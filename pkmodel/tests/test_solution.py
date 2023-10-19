import unittest
import pkmodel as pk

import matplotlib.pylab as plt
import numpy as np
import scipy.integrate

import numpy.testing as npt

from functools import partial

'''Some original functions we will use to test'''
def dose(t, X):
    return X

def rhs(t, y, Q_p1, V_c, V_p1, CL, X):
    q_c, q_p1 = y
    transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
    dqc_dt = dose(t, X) - q_c / V_c * CL - transition
    dqp1_dt = transition
    return [dqc_dt, dqp1_dt]


class SolutionTest(unittest.TestCase):
    """
    Tests the :class:`Solution` class.
    """
    def test_create(self):
        """
        Tests Solution creation.
        """
        model = pk.Model('test_name')
        solution = pk.Solution(model)
        self.assertEqual(solution.models[-1].name, 'test_name')

    def test_correct_output(self):

        t_eval = np.linspace(0, 1, 1000)
        y0 = np.array([0.0, 0.0])

        model = {
        'name': 'model',
        'Q_p1': 1.0,
        'V_c': 1.0,
        'V_p1': 1.0,
        'CL': 1.0,
        'X': 1.0,
        }

        args = [
            model['Q_p1'], model['V_c'], model['V_p1'], model['CL'], model['X']
        ]
        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: rhs(t, y, *args),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0, t_eval=t_eval
        )

        ############### NOW WE DO THE TEST

        test_model = pk.Model(name='test_model')
        test_model.add_compartment(name='dose', k_rate=1)
        test_model.add_compartment(name='peripheral', volume=1, k_rate=1)
        test_model.add_compartment(name='central', volume=1, k_rate=1)

        test_model.add_protocol(name='intravenous', dose=partial(dose,X=1))

        test_solution = test_model.solve(t_eval=t_eval, q0=y0)

        npt.assert_array_equal(sol.y, test_solution.y, verbose=True)



