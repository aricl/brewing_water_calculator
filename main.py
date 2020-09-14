import numpy as np

import input_water_profile as iwp
from additions.ams import get_ams_concentrations as ams
from additions.calcium_chloride import get_calcium_chloride_concentrations as calcium_chloride
from additions.calcium_sulphate import get_calcium_sulphate_concentrations as calcium_sulphate
from additions.dwb import get_dwb_concentrations as dwb
from additions.magnesium_sulphate import get_magnesium_sulphate_concentrations as magnesium_sulphate
from additions.sodium_chloride import get_sodium_chloride_concentrations as sodium_chloride

print('Please enter your initial water profile:')

initial_water_profile = iwp.input_water_profile()

print('Now please enter your target water profile:')

target_water_profile = iwp.input_water_profile()

water_profile_difference = np.subtract(target_water_profile, initial_water_profile)
print(water_profile_difference)

matrix = np.transpose(np.array([ams(), calcium_chloride(), calcium_sulphate(), dwb(), magnesium_sulphate(), sodium_chloride()]))

result = np.linalg.solve(matrix, water_profile_difference)

print(result)
print(matrix.dot(np.linalg.solve(matrix, water_profile_difference)) - water_profile_difference)
