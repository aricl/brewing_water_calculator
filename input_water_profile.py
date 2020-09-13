import numpy as np
import input_concentration as ic


def input_water_profile():
    ph = ic.input_concentration('pH (a.k.a. hydrogen ion concentration): ')
    chloride_concentration = ic.input_concentration('Chloride (Cl): ')
    sulphate_concentration = ic.input_concentration('Sulphate (SO4): ')
    total_hardness_as_carbonate_concentration = ic.input_concentration('Hardness Total as calcium carbonate (CaCO3): ')
    alkalinity_as_carbonate_concentration = ic.input_concentration('Alkalinity as calcium carbonate (CaCO3): ')
    sodium_concentration = ic.input_concentration('Sodium (Na): ')

    initial_water_profile = np.array([
        ph,
        chloride_concentration,
        sulphate_concentration,
        total_hardness_as_carbonate_concentration,
        alkalinity_as_carbonate_concentration,
        sodium_concentration
    ])

    return initial_water_profile
