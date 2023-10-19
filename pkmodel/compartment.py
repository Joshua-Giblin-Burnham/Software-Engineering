#
# Compartment class
#

class Compartment:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """

    def __init__(self, name, volume=None, k_rate=None, q0 = 0 ):
        self.name = name
        self.volume = volume
        self.k_rate = k_rate
        self.q0 = q0
           










