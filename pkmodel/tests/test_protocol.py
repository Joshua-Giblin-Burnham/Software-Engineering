import unittest
import pkmodel as pk
import numpy as np

def dose(t, X):
    return X

class ProtocolTest(unittest.TestCase):
    """
    Tests the :class:`Protocol` class.
    """
    def test_create(self):
        """
        Tests Protocol creation.
        """
        protocol = pk.Protocol(name ='subcutaneous', dose=dose, compartments=[])
        self.assertEqual(protocol.name, 'subcutaneous')

    def test_wrong_name(self):
        """
        Tests putting the wrong name.
        """

        with self.assertRaises(ValueError) as cm:
            protocol = pk.Protocol(name ='Jeff', dose=dose, compartments=[])

        self.assertEqual('Not accepted protocol label, must be intravenous or subcutaneous', str(cm.exception))