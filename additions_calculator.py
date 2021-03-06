import numpy as np
import additions.ams as ams
import additions.calcium_chloride as calcium_chloride
import additions.calcium_sulphate as calcium_sulphate
import additions.dwb as dwb
import additions.magnesium_sulphate as magnesium_sulphate
import additions.sodium_chloride as sodium_chloride
import additions.lactic_acid as lactic_acid
from scipy.optimize import minimize

TOLERANCE = 1e-2


def calculate_additions(initial_water_profile: np.array, target_water_profile: np.array) -> dict:
    water_profile_difference = np.subtract(target_water_profile, initial_water_profile)

    matrix = np.transpose(
        np.array([
            ams.get_concentrations(),
            calcium_chloride.get_concentrations(),
            calcium_sulphate.get_concentrations(),
            dwb.get_concentrations(),
            magnesium_sulphate.get_concentrations(),
            sodium_chloride.get_concentrations(),
            lactic_acid.get_concentrations()
        ])
    )

    def error_function(x) -> float:
        dot = matrix.dot(x)
        number_of_ions = len(dot)
        difference = dot - water_profile_difference
        mean_square = np.sum(difference ** 2) / number_of_ions
        root_mean_square = np.sqrt(mean_square)
        return root_mean_square

    initial_additions = np.array([1, 1, 1, 1, 1, 1, 1])
    bounds = ((0, None), (0, None), (0, None), (0, None), (0, None), (0, None), (0, None))
    result = minimize(error_function, initial_additions, method='SLSQP', tol=TOLERANCE, bounds=bounds)
    calculated_additions = result.x
    # calculated_additions = np.linalg.solve(matrix, water_profile_difference)

    additions = {
        'ams': calculated_additions[0],
        'calcium_chloride': calculated_additions[1],
        'calcium_sulphate': calculated_additions[2],
        'dwb': calculated_additions[3],
        'magnesium_sulphate': calculated_additions[4],
        'sodium_chloride': calculated_additions[5],
        'lactic_acid': calculated_additions[6]
    }

    return additions
