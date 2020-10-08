import numpy as np
import input_float as ic


def input_water_profile() -> np.array:
    calcium_concentration = ic.input_float('Calcium (Ca, ppm): ')
    chloride_concentration = ic.input_float('Chloride (Cl, ppm): ')
    sulphate_concentration = ic.input_float('Sulphate (SO4, ppm): ')
    alkalinity_as_carbonate_concentration = ic.input_float('Alkalinity as calcium carbonate (CaCO3, ppm): ')
    sodium_concentration = ic.input_float('Sodium (Na, ppm): ')
    magnesium_concentration = ic.input_float('Magnesium (Mg, ppm): ')

    water_profile = np.array([
        calcium_concentration,
        chloride_concentration,
        sulphate_concentration,
        alkalinity_as_carbonate_concentration,
        sodium_concentration,
        magnesium_concentration
    ])

    return water_profile
