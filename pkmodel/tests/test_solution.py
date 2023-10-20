import unittest
import pkmodel as pk


class SolutionTest(unittest.TestCase):
    """
    Tests the :class:`Solution` class.
    """
    def test_create(self):
        """
        Tests creation of instance of 'Solution' class.
        """
        model = pk.Model('test_name')
        solution = pk.Solution(model)
        self.assertEqual(solution.models[-1].name, 'test_name')



