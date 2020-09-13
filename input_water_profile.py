import numpy as np
import input_concentration as ic


def input_water_profile():
    calcium_concentration = ic.input_concentration('Calcium (Ca, ppm): ')
    chloride_concentration = ic.input_concentration('Chloride (Cl, ppm): ')
    sulphate_concentration = ic.input_concentration('Sulphate (SO4, ppm): ')
    alkalinity_as_carbonate_concentration = ic.input_concentration('Alkalinity as calcium carbonate (CaCO3, ppm): ')
    sodium_concentration = ic.input_concentration('Sodium (Na, ppm): ')
    magnesium_concentration = ic.input_concentration('Magnesium (Mg, ppm): ')

    water_profile = np.array([
        calcium_concentration,
        chloride_concentration,
        sulphate_concentration,
        alkalinity_as_carbonate_concentration,
        sodium_concentration,
        magnesium_concentration
    ])

    return water_profile
