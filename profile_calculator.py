from additions.ams import get_concentrations as ams
from additions.calcium_chloride import get_concentrations as calcium_chloride
from additions.calcium_sulphate import get_concentrations as calcium_sulphate
from additions.dwb import get_concentrations as dwb
from additions.magnesium_sulphate import get_concentrations as magnesium_sulphate
from additions.sodium_chloride import get_concentrations as sodium_chloride
import numpy as np


def calculate_profile(initial_water_profile: np.array, addition_concentrations: dict) -> np.array:
    final_water_profile = (
            initial_water_profile
            + (addition_concentrations['ams'] * ams())
            + (addition_concentrations['calcium_chloride'] * calcium_chloride())
            + (addition_concentrations['calcium_sulphate'] * calcium_sulphate())
            + (addition_concentrations['dwb'] * dwb())
            + (addition_concentrations['magnesium_sulphate'] * magnesium_sulphate())
            + (addition_concentrations['sodium_chloride'] * sodium_chloride())
    )

    return final_water_profile
