import unittest
import pkmodel as pk


#Useful function for creating compartments
def create_compartment(name, volume, k_rate, q0=0):
    test_compartment = pk.Compartment(name=name, volume=volume, k_rate=k_rate, q0=q0)


class CompartmentTest(unittest.TestCase):
    """
    Tests the :class:`Compartment` class.
    """

    def test_compartment_volume_exception(self):
        #tests exception is thrown if no volume given

        with self.assertRaises(ValueError) as cm:
            create_compartment(name='test', volume=None, k_rate=1.0)

        self.assertEqual('Volume must be set for this compartment', str(cm.exception))

    def test_compartment_transition_exception(self):
        #tests exception is thrown if no transition rate given

        with self.assertRaises(ValueError) as cm:
            create_compartment(name='test', volume=1.0, k_rate=None)

        self.assertEqual('Transition rate must be set for this compartment', str(cm.exception))


    def test_compartment_negative_volume_exception(self):
        #tests exception is thrown if negative volume given

        with self.assertRaises(ValueError) as cm:
            create_compartment(name='test', volume=-1, k_rate=1)

        self.assertEqual('Volume must be greater than zero', str(cm.exception))


    def test_compartment_negative_initial_drug_exception(self):
        #tests exception is thrown if negative intial drug amount

        with self.assertRaises(ValueError) as cm:
            create_compartment(name='test', volume=1, k_rate=1, q0=-1)

        self.assertEqual('Initial drug quantity must be greater than zero', str(cm.exception))
