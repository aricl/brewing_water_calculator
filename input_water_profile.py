import numpy as np
import input_concentration as ic


def input_water_profile():
    ph = ic.input_concentration('pH: ')
    chloride_concentration = ic.input_concentration('Chloride (Cl, ppm): ')
    sulphate_concentration = ic.input_concentration('Sulphate (SO4, ppm): ')
    total_hardness_as_carbonate_concentration = ic.input_concentration('Hardness as calcium carbonate (CaCO3, ppm): ')
    alkalinity_as_carbonate_concentration = ic.input_concentration('Alkalinity as calcium carbonate (CaCO3, ppm): ')
    sodium_concentration = ic.input_concentration('Sodium (Na, ppm): ')

    water_profile = np.array([
        ph,
        chloride_concentration,
        sulphate_concentration,
        total_hardness_as_carbonate_concentration,
        alkalinity_as_carbonate_concentration,
        sodium_concentration
    ])

    return water_profile
