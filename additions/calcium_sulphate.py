import numpy as np
from ions.atomic_mass_units import calcium, sulphate, water


def get_concentrations() -> np.array:
    """
        a.k.a. gypsum
        Key: Ca, Cl, SO4, alkalinity, Na, Mg
        The effect of 1g of CaSO4 on 1 litre of liquor in ppm
    :return: np.array
    """
    calcium_sulphate = calcium() + sulphate()
    ratio = 2

    return np.array([
        1000 * calcium() / (calcium_sulphate + ratio * water()),
        0,
        1000 * sulphate() / (calcium_sulphate + ratio * water()),
        0,
        0,
        0
    ])


def to_string(grams_per_litre: float) -> str:
    return str(round(grams_per_litre, 2)) + 'g/L'

