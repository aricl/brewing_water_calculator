import numpy as np


def get_calcium_chloride_concentrations():
    """
        Key: Ca, Cl, SO4, alkalinity, Na, Mg
        The effect of 1g of CaSO4 on 1 litre of liquor
        All values have been rounded to the nearest ppm
    :return: np.array
    """
    return np.array([218, 0, 524, 0, 0, 0])
