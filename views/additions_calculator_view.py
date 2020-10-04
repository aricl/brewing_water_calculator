import input_water_profile as iwp
from additions_calculator import calculate_additions
import additions.ams as ams
import additions.calcium_chloride as calcium_chloride
import additions.calcium_sulphate as calcium_sulphate
import additions.dwb as dwb
import additions.magnesium_sulphate as magnesium_sulphate
import additions.sodium_chloride as sodium_chloride
import additions.lactic_acid as lactic_acid


def view():
    print('Please enter your initial water profile:')
    initial_water_profile = iwp.input_water_profile()

    print('Now please enter your target water profile:')
    target_water_profile = iwp.input_water_profile()

    calculated_additions = calculate_additions(initial_water_profile, target_water_profile)
    calculated_additions_display = {
        'ams': ams.to_string(calculated_additions['ams']),
        'calcium_chloride': calcium_chloride.to_string(calculated_additions['calcium_chloride']),
        'calcium_sulphate': calcium_sulphate.to_string(calculated_additions['calcium_sulphate']),
        'dwb': dwb.to_string(calculated_additions['dwb']),
        'magnesium_sulphate': magnesium_sulphate.to_string(calculated_additions['magnesium_sulphate']),
        'sodium_chloride': sodium_chloride.to_string(calculated_additions['sodium_chloride']),
        'lactic_acid': lactic_acid.to_string(calculated_additions['lactic_acid'])
    }

    print(calculated_additions_display)
