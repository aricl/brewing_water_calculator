import input_water_profile as iwp
import profile_calculator
from input_float import input_float


def view():
    print('Please enter your initial water profile:')
    initial_water_profile = iwp.input_water_profile()

    print('Now please enter your additions:')
    additions_concentrations = {
        'ams': input_float('AMS (mL/L): '),
        'calcium_chloride': input_float('Calcium Chloride (g/L): '),
        'calcium_sulphate': input_float('Calcium Sulphate (g/L): '),
        'dwb': input_float('DWB (g/L): '),
        'magnesium_sulphate': input_float('Magnesium Sulphate, a.k.a. Epsom salts (g/L): '),
        'sodium_chloride': input_float('Sodium chloride, a.k.a. table salt (g/L): ')
    }

    final_water_profile = profile_calculator.calculate_profile(
        initial_water_profile,
        additions_concentrations
    )

    final_water_profile_view = {
        'Calcium (Ca, ppm): ': round(final_water_profile[0], 2),
        'Chloride (Cl, ppm): ': round(final_water_profile[1], 2),
        'Sulphate (SO4, ppm): ': round(final_water_profile[2], 2),
        'Alkalinity as calcium carbonate (CaCO3, ppm): ': round(final_water_profile[3], 2),
        'Sodium (Na, ppm): ': round(final_water_profile[4], 2),
        'Magnesium (Mg, ppm): ': round(final_water_profile[5], 2)
    }

    print(final_water_profile_view)
