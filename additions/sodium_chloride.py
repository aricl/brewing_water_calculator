import numpy as np


def get_sodium_chloride_concentrations():
    """
        Key: Ca, Cl, SO4, alkalinity, Na, Mg
        The effect of 1g of NaCl on 1 litre of liquor
        All values have been rounded to the nearest ppm
    :return: np.array
    """
    return np.array([0, 614, 0, 0, 403, 0])
