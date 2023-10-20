import unittest
import pkmodel as pk
import pathlib as pl
import numpy as np


class PlotTest(unittest.TestCase):
    """
    Tests the :class:`Solution` class outputs files.
    """
    def test_create(self):
        """
        Tests file creation.
        """
        
        path = pl.Path('plots/plot.png')
        self.assertTrue(path.is_file())

