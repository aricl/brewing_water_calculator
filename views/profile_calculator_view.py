import input_water_profile as iwp
from additions_calculator import calculate_additions
from input_float import input_float
from additions.ams import get_concentrations as ams
from additions.calcium_chloride import get_concentrations as calcium_chloride
from additions.calcium_sulphate import get_concentrations as calcium_sulphate
from additions.dwb import get_concentrations as dwb
from additions.magnesium_sulphate import get_concentrations as magnesium_sulphate
from additions.sodium_chloride import get_concentrations as sodium_chloride


def view():
    print('Please enter your initial water profile:')
    initial_water_profile = iwp.input_water_profile()

    print('Now please enter your additions:')
    ams_concentration = input_float('AMS (mL/L): ')
    calcium_chloride_concentration = input_float('Calcium Chloride (g/L): ')
    calcium_sulphate_concentration = input_float('Calcium Sulphate (g/L): ')
    dwb_concentration = input_float('DWB (g/L): ')
    magnesium_sulphate_concentration = input_float('Magnesium Sulphate, a.k.a. Epsom salts (g/L): ')
    sodium_chloride_concentration = input_float('Sodium chloride, a.k.a. table salt (g/L): ')

    final_water_profile = (
        initial_water_profile
        + (ams_concentration * ams())
        + (calcium_chloride_concentration * calcium_chloride())
        + (calcium_sulphate_concentration * calcium_sulphate())
        + (dwb_concentration * dwb())
        + (magnesium_sulphate_concentration * magnesium_sulphate())
        + (sodium_chloride_concentration * sodium_chloride())
    )

    final_water_profile_view = {
        'Calcium (Ca, ppm): ': final_water_profile[0],
        'Chloride (Cl, ppm): ': final_water_profile[1],
        'Sulphate (SO4, ppm): ': final_water_profile[2],
        'Alkalinity as calcium carbonate (CaCO3, ppm): ': final_water_profile[3],
        'Sodium (Na, ppm): ': final_water_profile[4],
        'Magnesium (Mg, ppm): ': final_water_profile[5]
    }

    print(final_water_profile_view)
