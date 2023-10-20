import unittest
import pkmodel as pk
import numpy.testing as npt
import matplotlib.pylab as plt
import numpy as np
import scipy.integrate
from functools import partial

#Some functions from the original code we will use to test our new one
def dose(t, X):
    return X

def rhs(t, y, Q_p1, V_c, V_p1, CL, X):
    q_c, q_p1 = y
    transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
    dqc_dt = dose(t, X) - q_c / V_c * CL - transition
    dqp1_dt = transition
    return [dqc_dt, dqp1_dt]


class ModelTest(unittest.TestCase):
    """
    Tests the :class:`Model` class.
    """
    def test_create(self):
        """
        Tests Model creation.
        """
        model = pk.Model('test_name')

        self.assertEqual(model.name, 'test_name')

    def test_correct_output(self):
        """
        Tests that the model gives the correct values as the original code 
        """

        #Set up the parameters for the test

        t_eval = np.linspace(0, 1, 1000)
        y0 = np.array([0.0, 0.0])

        X=1.0

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

        #compute the solution using the original code#

        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: rhs(t, y, *args),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0, t_eval=t_eval
        )

        #now use our new code to create a Model class
        test_model = pk.Model(name='test_model')

        #add the relevant compartments for an intravenous model

        test_model.add_compartment(name='peripheral1', volume=1, k_rate=1)
        test_model.add_compartment(name='central', volume=1, k_rate=1)

        #add the correct protocol, with the dose function defined above
        test_model.add_protocol('intravenous', dose)

        #compute the solution, and return the value of the solution. 'X' the constant dose amount is supplied
        test_solution = test_model.solve(t_eval, X, return_sol=True)

        #check that the output solution arrays are completely equal
        npt.assert_array_equal(sol.y, test_solution.y, verbose=True)
        

    
