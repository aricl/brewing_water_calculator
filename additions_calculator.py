import numpy as np
from additions.ams import get_ams_concentrations as ams
from additions.calcium_chloride import get_calcium_chloride_concentrations as calcium_chloride
from additions.calcium_sulphate import get_calcium_sulphate_concentrations as calcium_sulphate
from additions.dwb import get_dwb_concentrations as dwb
from additions.magnesium_sulphate import get_magnesium_sulphate_concentrations as magnesium_sulphate
from additions.sodium_chloride import get_sodium_chloride_concentrations as sodium_chloride


def calculate_additions(initial_water_profile, target_water_profile):
    water_profile_difference = np.subtract(target_water_profile, initial_water_profile)

    matrix = np.transpose(
        np.array([
            ams(),
            calcium_chloride(),
            calcium_sulphate(),
            dwb(),
            magnesium_sulphate(),
            sodium_chloride()
        ])
    )

    return np.linalg.solve(matrix, water_profile_difference)
