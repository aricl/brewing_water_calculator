import input_water_profile as iwp
from additions_calculator import calculate_additions

print('Please enter your initial water profile:')

initial_water_profile = iwp.input_water_profile()

print('Now please enter your target water profile:')

target_water_profile = iwp.input_water_profile()

result = calculate_additions(initial_water_profile, target_water_profile)

print(result)
