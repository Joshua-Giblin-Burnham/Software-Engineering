import unittest
import pkmodel as pk
import numpy as np


class ProtocolTest(unittest.TestCase):
    """
    Tests the :class:`Protocol` class.
    """
    def test_create(self):
        """
        Tests Protocol creation.
        """
        protocol = pk.Protocol(name ='subcutaneous', dose=2, compartments=[])
        self.assertEqual(protocol.name, 'subcutaneous')

