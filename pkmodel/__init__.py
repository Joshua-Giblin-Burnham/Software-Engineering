"""pkmodel is a Pharmokinetic modelling library.

It contains functionality for creating, solving, and visualising the solution
of Parmokinetic (PK) models

"""
# Import required standard librarys
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate

# Import version info
from .version_info import VERSION_INT, VERSION  # noqa

# Import main classes
from .compartment import Compartment     # noqa
from .model import Model    # noqa
from .protocol import Protocol    # noqa
from .solution import Solution     # noqa
