import numpy as np


def get_ams_concentrations():
    """
        Key: ph, Cl, SO4, hardness, alkalinity, Na
        The effect of 1mL of AMS on 1 litre of liquor
        Note: I have left the effect on hardness and pH as zero
        This is because the data-sheet for AMS does not provide these
        values. I would like to find out if possible
    :return: np.array
    """
    return np.array([0, 65, 90, 0, -185, 0])
