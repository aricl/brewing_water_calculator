import numpy as np

import input_water_profile as iwp

print('Please enter your initial water profile:')

initial_water_profile = iwp.input_water_profile()

print('Now please enter your target water profile:')

target_water_profile = iwp.input_water_profile()

water_profile_difference = np.subtract(target_water_profile, initial_water_profile)
print(water_profile_difference)
