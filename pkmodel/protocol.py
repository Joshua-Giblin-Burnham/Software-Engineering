#
# Protocol class
#
import numpy as np

class Protocol:
    """A Pharmokinetic (PK) protocol defines the dising protocol and defines corresponding form the right-hand side of the PK ODE.

    Parameters
    ----------
        :param name: Name of protocol, either subcutaneous or intravenous.
        :type name: string
        :param compartments:  Dictionary of compartments/ classes holding classes.
        :type name: list
        :param dose: Dose function defining how dose changes over time
        :type dose: Function
    """

    # Initialise protocol defining dose function, name(i.e. type), and compartments the model holds
    def __init__(self, name, compartments, dose):
        if name != 'subcutaneous' or name != 'intravenous': 
            ValueError('Not accepted protocol label, must be intravenous or subcutaneous')
        else:
            self.name = name
            self.compartments = compartments
            self.dose = dose

    # Define RHS function
    def rhs(self, t, q, *args): 
        """ Defines corresponding form of the right-hand side of the PK ODE.
        Parameters
        ----------
        :param t: Time parameter of model. 
        :type t: arr
        :param q: Ndim-vector representing quantities of drug (qi) across N compartments, first value quantity for central compartment, if dose compartment given it is set as last value 
        :type q: arr
        :param args: Arguments to pass to dose function
        :type args: None

        :return rhs_ib: RHS of ODE for the model
        """ 
        # Extraxt central and perpheral compartments 
        cent_cmpt        = self.compartments['central'][0]
        peripheral_cmpts = self.compartments['peripheral']

        # Define transition N-vector representing drug transitions between central and each N perpheral compartments
        transition = [( q[0]/cent_cmpt.volume - q[i+1] / p_cmpt.volume) * p_cmpt.k_rate 
                     for i, p_cmpt in enumerate(peripheral_cmpts)]

        # Check protocal type, returning corresponding rhs
        if self.name == 'subcutaneous':

            # Check that dosing compartment is given
            if len(self.compartments['dose'])!=0:
                # Extract dose compartment
                dose_cmpt = self.compartments['dose'][0]
                
                # Set dose quantity differential, using compartment variables and dose function
                qd_dot  = self.dose(t, *args) - dose_cmpt.k_rate*q[-1]

                # Central differential proportional to sum of N perpheral transitions
                qc_dot  = np.array([dose_cmpt.k_rate*q[-1] - q[0]*cent_cmpt.k_rate/cent_cmpt.volume - sum(transition)])

                # N peripheral differentials proportional to each corresponding N transiton
                qpi_dot = np.array(transition)

                return np.hstack((qc_dot, qpi_dot, qd_dot))
            
            # Raise error is dose compartment not added
            else:
                ValueError('Subcutaneous protocol requires dosing compartment')

        elif self.name == 'intravenous': 
            # Central differential proportional to sum of N perpheral transitions
            qc_dot = np.array([self.dose(t, *args) - q[0]*cent_cmpt.k_rate/cent_cmpt.volume - sum(transition)])
            # N peripheral differentials proportional to each corresponding N transiton
            qpi_dot = np.array(transition)

            return np.hstack((qc_dot, qpi_dot))
        
        # Error if dosing label incorrect
        else:
            ValueError('Not accepted dosing label, must be intravenous or subcutaneous')
        
            