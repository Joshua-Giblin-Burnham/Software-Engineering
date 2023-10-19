#
# Model class
#

import scipy.integrate
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
                             'dose' : [], 
                             'peripheral' : []
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

    def solve(self, t_eval, q0, *arg):
        
        rhs = self.protocol[-1].rhs
        solution = scipy.integrate.solve_ivp(fun = lambda t, q : rhs(t, q, *arg),
                                        t_span = [t_eval[0], t_eval[-1]],
                                        y0 = q0, t_eval = t_eval )
        self.solution = solution
        
        return solution
    
