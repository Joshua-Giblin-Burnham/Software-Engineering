#
# Model class
#

import scipy.integrate
from .protocol import Protocol

class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    value: numeric, optional
        an example paramter
    """

    def __init__(self, name, Q_p1=2.0, V_c=1.0, V_p1=1.0, CL=1.0, X=1.0, k_a=None ):

        self.name = name
        self.protocol = []

        self.Q_p1 = Q_p1
        self.V_c  = V_c
        self.V_p1 = V_p1
        self.CL   = CL
        self.X    = X

        if k_a != None:
            self.k_a = k_a        

    # @property
    # def arg(self):
    #     args = self.__dict__
    #     args.pop("name")
    #     args.pop("protocal")
    #     return list(args.values)

    def add_protocols(self, dose, name):
        self.protocol.append(Protocol(dose, name))

    def solve(self, t_eval, y0):
        args = list(self.__dict__.values())[2:]
        rhs = self.protocol[-1].rhs
        sol = scipy.integrate.solve_ivp(fun=lambda t, y: rhs(t, y, args),
                                        t_span=[t_eval[0], t_eval[-1]],
                                        y0=y0, t_eval=t_eval )
        
        return sol