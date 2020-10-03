import unittest
import numpy as np
import additions_calculator


class MyTestCase(unittest.TestCase):
    def test_kernel_ales_bitters_ipas_water_profile(self):
        # Ca, Cl, SO4, Alkalinity as CO3, Na, Mg
        initial_water_profile = np.array([87.36, 43.74, 52.3, 190, 0.0, 5.09])
        target_water_profile = np.array([196.36, 207.74, 355.3, 30, 0.0, 8.39])

        calculated_additions = additions_calculator.calculate_additions(
            initial_water_profile,
            target_water_profile
        )

        expected_additions = {
            'ams': '0.86mL/L',
            'calcium_chloride': '0.0g/L',
            'calcium_sulphate': '0.0g/L',
            'dwb': '0.61g/L',
            'magnesium_sulphate': '0.0g/L',
            'sodium_chloride': '0.0g/L',
            'lactic_acid': '0.0mL/L'
        }

        self.assertEqual(expected_additions, calculated_additions)

    def test_kernel_lagers_pilsners_water_profile(self):
        # Ca, Cl, SO4, Alkalinity as CO3, Na, Mg
        initial_water_profile = np.array([87.36, 43.74, 52.3, 190, 0.0, 5.09])
        target_water_profile = np.array([133.49, 94.14, 93.90, 34, 0.0, 5.09])

        calculated_additions = additions_calculator.calculate_additions(
            initial_water_profile,
            target_water_profile
        )

        expected_additions = {
            'ams': '0.0mL/L',
            'calcium_chloride': '0.11g/L',
            'calcium_sulphate': '0.07g/L',
            'dwb': '0.0g/L',
            'magnesium_sulphate': '0.0g/L',
            'sodium_chloride': '0.0g/L',
            'lactic_acid': '0.61mL/L'
        }

        self.assertEqual(expected_additions, calculated_additions)

    def test_kernel_stouts_porters_water_profile(self):
        # Ca, Cl, SO4, Alkalinity as CO3, Na, Mg
        initial_water_profile = np.array([87.36, 43.74, 52.3, 190, 0.0, 5.09])
        target_water_profile = np.array([134.36, 266.74, 99.30, 94.00, 66.9, 5.09])

        calculated_additions = additions_calculator.calculate_additions(
            initial_water_profile,
            target_water_profile
        )

        expected_additions = {
            'ams': '0.52mL/L',
            'calcium_chloride': '0.18g/L',
            'calcium_sulphate': '0.0g/L',
            'dwb': '0.0g/L',
            'magnesium_sulphate': '0.0g/L',
            'sodium_chloride': '0.17g/L',
            'lactic_acid': '0.0mL/L'
        }

        self.assertEqual(expected_additions, calculated_additions)

    def test_bermondsey_2020_to_achieve_balanced_profile(self):
        # Ca, Cl, SO4, Alkalinity as CO3, Na, Mg
        initial_water_profile = np.array([104, 49.2, 54.0, 184, 33.9, 4.8])
        # I got this profile from the first balanced profile:
        # https://www.brewersfriend.com/brewing-water-target-profiles/
        # The only change I have made is I modified the Ca, Na, and Mg
        # targets such that they match the initial profile, since the
        # differences are small.
        target_water_profile = np.array([104, 75, 80, 100, 33.9, 4.8])

        calculated_additions = additions_calculator.calculate_additions(
            initial_water_profile,
            target_water_profile
        )

        expected_additions = {
            'ams': '0.3mL/L',
            'calcium_chloride': '0.01g/L',
            'calcium_sulphate': '0.0g/L',
            'dwb': '0.0g/L',
            'magnesium_sulphate': '0.0g/L',
            'sodium_chloride': '0.0g/L',
            'lactic_acid': '0.11mL/L'
        }

        self.assertEqual(expected_additions, calculated_additions)


if __name__ == '__main__':
    unittest.main()
