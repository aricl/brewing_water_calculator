import numpy as np


def get_concentrations() -> np.array:
    """
        Key: Ca, Cl, SO4, alkalinity, Na, Mg
        The effect of 1mL of lactic acid on 1 litre of liquor
        All values have been rounded to the nearest ppm
    :return: np.array
    """
    return np.array([0, 0, 0, -255, 0, 0])


def to_string(millilitres_per_litre: float) -> str:
    return str(round(millilitres_per_litre, 2)) + 'mL/L'
