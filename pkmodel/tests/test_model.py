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
        model = pk.Model('BLANK')

        self.assertEqual(model.Q_p1, 2)

    def test_add_protocol(self):

        model = pk.Model('BLANK')
        model.add_protocols(dose=2, name='JEFF')
        self.assertEqual(model.protocol[0].name, 'JEFF')

    
