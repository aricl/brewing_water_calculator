import numpy as np
import additions.ams as ams
import additions.calcium_chloride as calcium_chloride
import additions.calcium_sulphate as calcium_sulphate
import additions.dwb as dwb
import additions.magnesium_sulphate as magnesium_sulphate
import additions.sodium_chloride as sodium_chloride


def calculate_additions(initial_water_profile, target_water_profile):
    water_profile_difference = np.subtract(target_water_profile, initial_water_profile)

    matrix = np.transpose(
        np.array([
            ams.get_concentrations(),
            calcium_chloride.get_concentrations(),
            calcium_sulphate.get_concentrations(),
            dwb.get_concentrations(),
            magnesium_sulphate.get_concentrations(),
            sodium_chloride.get_concentrations()
        ])
    )

    linear_decomposition_result = np.linalg.solve(matrix, water_profile_difference)
    additions = {
        'ams': ams.to_string(linear_decomposition_result[0]),
        'calcium_chloride': calcium_chloride.to_string(linear_decomposition_result[1]),
        'calcium_sulphate': calcium_sulphate.to_string(linear_decomposition_result[2]),
        'dwb': dwb.to_string(linear_decomposition_result[3]),
        'magnesium_sulphate': magnesium_sulphate.to_string(linear_decomposition_result[4]),
        'sodium_chloride': sodium_chloride.to_string(linear_decomposition_result[5])
    }

    return additions
