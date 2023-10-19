#
# Compartment class
#

class Compartment:
    """A Pharmokinetic (PK) compartment used in a given model type. Holds compartment data.

    :param name: Name/Type of compartment - must be either central, dose, or peripheral_X.
    :type name: string
    :param volume: Volume of compartment, mush be positive.
    :type volume: float
    :param k_rate: Transition rate out of a given compartment. Depending on compartment type is CL, k_a, or Q_Pi.
    :type k_rate: float
    :param q0: Initial quantity of drug in compartment.
    :type q0: float
    """

    def __init__(self, name, volume=None, k_rate=None, q0 = 0 ):
        # Ensure that volume and q0 values are feasible
        if volume!=None and volume < 0:
            raise ValueError("Volume must be greater than zero")
        elif q0 < 0:
            raise ValueError("Initial drug quantity must be greater than zero")
        else:
            # Set Compartment variables
            self.name = name
            self.volume = volume
            self.k_rate = k_rate
            self.q0 = q0
            










