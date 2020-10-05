import numpy as np
from ions.atomic_mass_units import calcium, chlorine, water


def get_concentrations() -> np.array:
    """
        Key: Ca, Cl, SO4, alkalinity, Na, Mg
        The effect of 1g of CaCl on 1 litre of liquor in ppm
    """
    calcium_chloride = calcium() + (2 * chlorine())
    ratio = 2.35

    return np.array([
        (1000 * calcium()) / (calcium_chloride + ratio * water()),
        (1000 * 2 * chlorine()) / (calcium_chloride + ratio * water()),
        0,
        0,
        0,
        0
    ])


def to_string(grams_per_litre: float) -> str:
    return str(round(grams_per_litre, 2)) + 'g/L'
