import unittest
import pkmodel as pk


class ProtocolTest(unittest.TestCase):
    """
    Tests the :class:`Protocol` class.
    """
    def test_create(self):
        """
        Tests Protocol creation.
        """
        protocol = pk.Protocol(name ='test_protocol', dose=2, compartments=[])
        self.assertEqual(protocol.name, 'test_protocol')

