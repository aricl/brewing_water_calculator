import numpy as np
from ions.atomic_mass_units import sodium, chlorine


def get_concentrations():
    """
        Key: Ca, Cl, SO4, alkalinity, Na, Mg
        The effect of 1g of NaCl on 1 litre of liquor in ppm
    :return: np.array
    """
    sodium_chloride = sodium() + chlorine()

    return np.array([
        0,
        1000 * chlorine() / sodium_chloride,
        0,
        0,
        1000 * sodium() / sodium_chloride,
        0
    ])


def to_string(grams_per_litre):
    return str(round(grams_per_litre, 2)) + 'g/L'

