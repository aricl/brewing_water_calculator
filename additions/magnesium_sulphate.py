import numpy as np


def get_magnesium_sulphate_concentrations():
    """
        a.k.a. Epsom salts
        Key: Ca, Cl, SO4, alkalinity, Na, Mg
        The effect of 1g of MgSO4 on 1 litre of liquor
        All values have been rounded to the nearest ppm
    :return: np.array
    """
    return np.array([0, 0, 390, 0, 0, 98])
