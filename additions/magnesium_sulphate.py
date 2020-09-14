import numpy as np
from ions.atomic_mass_units import magnesium, sulphate, water


def get_magnesium_sulphate_concentrations():
    """
        a.k.a. Epsom salts
        Key: Ca, Cl, SO4, alkalinity, Na, Mg
        The effect of 1g of MgSO4 on 1 litre of liquor in ppm
    :return: np.array
    """
    magnesium_sulphate = magnesium() + sulphate()
    ratio = 7

    return np.array([
        0,
        0,
        1000 * sulphate() / (magnesium_sulphate + ratio * water()),
        0,
        0,
        1000 * magnesium() / (magnesium_sulphate + ratio * water())
    ])
