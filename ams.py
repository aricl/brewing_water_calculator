import numpy as np


def get_ams_concentrations():
    """
        Key: Cl, SO4, alkalinity, Na
        The effect of 1mL of AMS on 1 litre of liquor
    :return: np.array
    """
    return np.array([65, 90, -185, 0])
