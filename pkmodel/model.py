#
# Model class
#

# Import required modules
import scipy.integrate
import numpy as np
from .protocol import Protocol
from .compartment import Compartment

class Model:
    """A Pharmokinetic (PK) model that contain defines drug compartments, dosing protocol and holds solutions. 

    Parameters
    ----------
    :param name: Name of model
    :type name: string
    """

    # Initialise class variables, holds model name, sets up compartment structure
    def __init__(self, name = 'pkmodel'):
        self.name = name

        # Compartments are defined in dictionary structure
        self.compartments = {'central' : [], 
                             'peripheral' : [],                             
                             'dose' : []
                             }
        # Creates empty protocol to easily append new protocal
        self.protocol = [] 
        self.solution = None   


    def add_compartment(self, name, **kwargs):
        """ Append new compartment to corresponding compartment dictionary.

        Parameters
        ---------- 
        :param name: Name of compartment, must be correctly formatted to add to dictionary correctly must be either central, dose, or peripheral_X.
        :type name: string
        
        :param kwargs: Keyword arguments for compartment to set compartment variables, i.e. volume, transition rate(k_rate), initial drug quantity(q0)
        :type kwargs: None
        """

        # Ensure only one central compartment is defined 
        if name == 'central' and len(self.compartments[name]) == 0 :
            self.compartments['central'].append(Compartment(name, **kwargs))
        
        # Ensure only one dosing compartment (could add extra dosing functionality)
        elif name == 'dose' and len(self.compartments[name]) == 0:
            self.compartments['dose'].append(Compartment(name, **kwargs))

        # Ensure all peripheral compartments follow peripheral_X name structure
        elif name[:10] == 'peripheral':
            self.compartments['peripheral'].append(Compartment(name, **kwargs))

        # Raise value error if invalide name given
        else:
            ValueError('Not accepted compartment choose: central, dosing or perpherial_X')


    def add_Ncompartments(self, N, **kwargs):
        """ Append  multiple new compartment to peripheral compartment dictionary.

        Parameters
        ---------- 
        :param N: Numbr of compartment
        :type N: int
        
        :param kwargs: Keyword arguments for compartment to set compartment variables, i.e. volume, transition rate(k_rate), initial drug quantity(q0)
        :type kwargs: None
        """
        Np = len(np.array(self.compartments['peripheral']))

        for i in range(Np,N+Np):
            self.compartments['peripheral'].append(Compartment('peripheral_'+str(i), **kwargs))
        

    def add_protocol(self, name, dose):
        """ Append new protocol for drug dosing, either subcutaneous or intravenous.
        Parameters
        ---------- 
        :param name: Name of protocol, either subcutaneous or intravenous.
        :type name: string
        
        :param dose: Dose function defining how dose changes over time
        :type dose: Function
        """
        # Append protocol class which internally defines rhs and apples dosing type
        self.protocol.append(Protocol(name, self.compartments, dose))


    def solve(self, t_eval, *args, **kwargs):
        """Finds solution of drug dosage over time for a given set of compartments, dose and transition/CL rates.

        Parameters
        ----------
        :param t_eval: Array of time points that model is solved for.
        :type t_eval: arr
        :param args: Arguments, if required, needed to passs to dose function.
        :type args: None
        :param kwargs: Keyword arguments for optional self definition of initial quantiies q0, and if solutions are returned
        """

        # If q0(initial quantities) defined as keyword argument use the inital conditions
        if 'q0' in kwargs:
            q0 = kwargs['q0']

        # Else set initial conditions using values defined/ extracted from each compartment
        else:
            q0 = np.array([compartment.q0 
                            for compartment_list in self.compartments.values() 
                            for compartment in compartment_list])
        
        # Extract RHS from protocol variable (which accounts for dosing protocol)
        rhs = self.protocol[-1].rhs

        # Uses scipy to integrate using RHS, initial condition and for given time points 
        solution = scipy.integrate.solve_ivp(fun = lambda t, q : rhs(t, q, *args),
                                        t_span = [t_eval[0], t_eval[-1]],
                                        y0 = q0, t_eval = t_eval )
        
        # Store solution
        self.solution = solution
        
        # If specified return solution
        if 'return_sol' in kwargs and kwargs['return_sol']==True:
            return solution
    
