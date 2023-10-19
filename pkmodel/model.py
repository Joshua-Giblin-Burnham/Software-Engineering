#
# Model class
#

import scipy.integrate
import numpy as np
from .protocol import Protocol
from .compartment import Compartment

class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    value: numeric, optional
        an example paramter
    """

    def __init__(self, name = 'pkmodel'):
        self.name = name
        self.compartments = {'central' : [], 
                             'peripheral' : [],                             
                             'dose' : []
                             }
        self.protocol = [] 
        self.solution = None   


    def add_compartment(self, name, **kwargs):
        if name == 'central' and len(self.compartments[name]) == 0 :
            self.compartments['central'].append(Compartment(name, **kwargs))
        
        elif name == 'dose' and len(self.compartments[name]) == 0:
            self.compartments['dose'].append(Compartment(name, **kwargs))

        elif name[:10] == 'peripheral':
            self.compartments['peripheral'].append(Compartment(name, **kwargs))

        else:
            ValueError('Not accepted compartment label')


    def add_protocol(self, name, dose):
        self.protocol.append(Protocol(name, self.compartments, dose))

    def solve(self, t_eval, *args, **kwargs):

        if 'q0' in kwargs:
            q0 = kwargs['q0']
        else:
            q0 = np.array([compartment.q0 
                        for compartment_list in self.compartments.values() 
                        for compartment in compartment_list])
            
        rhs = self.protocol[-1].rhs
        
        solution = scipy.integrate.solve_ivp(fun = lambda t, q : rhs(t, q, *args),
                                        t_span = [t_eval[0], t_eval[-1]],
                                        y0 = q0, t_eval = t_eval )
        self.solution = solution
        
        return solution
    
