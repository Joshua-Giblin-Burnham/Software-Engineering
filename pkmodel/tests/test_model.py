import unittest
import pkmodel as pk


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

    def test_add_protocol(self):
        #Tests adding a protocol to the model

        model = pk.Model('test_name')
        model.add_protocol(dose=2, name='test_protocol')
        self.assertEqual(model.protocol[0].name, 'test_protocol')
        

    
