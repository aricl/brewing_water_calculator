import numpy as np
from ions.atomic_mass_units import calcium, chlorine, water


def get_calcium_chloride_concentrations():
    """
        Key: Ca, Cl, SO4, alkalinity, Na, Mg
        The effect of 1g of CaCl on 1 litre of liquor in ppm
    :return: np.array
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
