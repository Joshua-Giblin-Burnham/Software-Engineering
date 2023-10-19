#
# Protocol class
#
import numpy as np

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """

    def __init__(self, name, compartments, dose):
        self.name = name
        self.compartments = compartments
        self.dose = dose

    def rhs(self, t, q, *arg): 
        cent_cmpt        = self.compartments['central'][0]
        peripheral_cmpts = self.compartments['peripheral']


        transition = [( q[0]/cent_cmpt.volume - q[i+1] / p_cmpt.volume) * p_cmpt.k_rate 
                     for i, p_cmpt in enumerate(peripheral_cmpts)]

        if self.name == 'subcutaneous' and  len(self.compartments['dose'])!=0:
            dose_cmpt = self.compartments['dose'][0]

            q0_dot  = self.dose(t, *arg) - dose_cmpt.k_rate*q[-1]
            qc_dot  = np.array([dose_cmpt.k_rate*q[-1] - q[0]*cent_cmpt.k_rate/cent_cmpt.volume - sum(transition)])
            qpi_dot = np.array(transition)

            return np.hstack((q0_dot, qc_dot, qpi_dot))
        
        elif self.name == 'intravenous': 
            qc_dot = np.array([self.dose(t, *arg) - q[0]*cent_cmpt.k_rate/cent_cmpt.volume - sum(transition)])
            qpi_dot = np.array(transition)

            return np.hstack((qc_dot, qpi_dot))
        
        else:
            ValueError('Not accepted dosing label')
        
            