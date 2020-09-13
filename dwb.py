import numpy as np


def get_dwb_concentrations():
    """
        Key: Ca, Cl, SO4, alkalinity, Na, Mg
        The effect of 1g of DWB on 1 litre of liquor
        All values have been rounded to the nearest ppm,
        except Mg since it is so small
    :return: np.array
    """
    return np.array([178, 177, 368, 0, 0, 5.4])