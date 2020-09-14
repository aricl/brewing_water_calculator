import numpy as np


def get_calcium_chloride_concentrations():
    """
        Key: Ca, Cl, SO4, alkalinity, Na, Mg
        The effect of 1g of CaCl on 1 litre of liquor
        All values have been rounded to the nearest ppm
    :return: np.array
    """
    return np.array([262, 458, 0, 0, 0, 0])
