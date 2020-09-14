import numpy as np


def get_concentrations():
    """
        Key: Ca, Cl, SO4, alkalinity, Na, Mg
        The effect of 1g of DWB on 1 litre of liquor
        All values have been rounded to the nearest ppm,
        except Mg since it is so small
    :return: np.array
    """
    return np.array([178, 177, 368, 0, 0, 5.4])


def to_string(grams_per_litre):
    return str(round(grams_per_litre, 2)) + 'g/L'

