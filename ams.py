import numpy as np


def get_ams_concentrations():
    """
        Key: Ca, Cl, SO4, alkalinity, Na
        The effect of 1mL of AMS on 1 litre of liquor
    :return: np.array
    """
    return np.array([0, 65, 90, -185, 0])
