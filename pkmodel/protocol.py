#
# Protocol class
#

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """

    def __init__(self, dose, name='intravenous'):
        self.name = name
        self.dose = dose

    def rhs(self, t, y, args): 
        if self.name == 'intravenous':
                Q_p1, V_c, V_p1, CL, X = args

                q_c, q_p1 = y
                transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)

                dqc_dt  = self.dose(t, X) - q_c / V_c * CL - transition
                dqp1_dt = transition

                return [dqc_dt, dqp1_dt]

        elif self.name == 'subcutaneous':
                Q_p1, V_c, V_p1, CL, X, k_a = args

                q_0, q_c, q_p1 = y

                transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)

                dq0_dt  = self.dose(t, X) - k_a*q_0
                dqc_dt  = k_a*q_0 - q_c / V_c * CL - transition
                dqp1_dt = transition

                return [dq0_dt, dqc_dt, dqp1_dt]