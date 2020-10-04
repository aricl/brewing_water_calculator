import unittest
import numpy as np
import additions_calculator


# TODO: Get the water profile calculated from the additions in each test. See how close
#       it gets to the difference between the target and initial profiles.
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
            'ams': 0.865,
            'calcium_chloride': 0.001,
            'calcium_sulphate': 0.004,
            'dwb': 0.606,
            'magnesium_sulphate': 0.000,
            'sodium_chloride': 0.000,
            'lactic_acid': 0.000
        }

        for key in expected_additions.keys():
            abs_diff = abs(expected_additions[key] - calculated_additions[key])
            self.assertLessEqual(
                abs_diff,
                additions_calculator.TOLERANCE,
                'The addition concentration ' + key + ' deviates too much from the expected value'
            )

    def test_kernel_lagers_pilsners_water_profile(self):
        # Ca, Cl, SO4, Alkalinity as CO3, Na, Mg
        initial_water_profile = np.array([87.36, 43.74, 52.3, 190, 0.0, 5.09])
        target_water_profile = np.array([133.49, 94.14, 93.90, 34, 0.0, 5.09])

        calculated_additions = additions_calculator.calculate_additions(
            initial_water_profile,
            target_water_profile
        )

        expected_additions = {
            'ams': 0.000,
            'calcium_chloride': 0.109,
            'calcium_sulphate': 0.075,
            'dwb': 0.000,
            'magnesium_sulphate': 0.000,
            'sodium_chloride': 0.000,
            'lactic_acid': 0.611
        }

        for key in expected_additions.keys():
            abs_diff = abs(expected_additions[key] - calculated_additions[key])
            self.assertLessEqual(
                abs_diff,
                additions_calculator.TOLERANCE,
                'The addition concentration ' + key + ' deviates too much from the expected value'
            )

    def test_kernel_stouts_porters_water_profile(self):
        # Ca, Cl, SO4, Alkalinity as CO3, Na, Mg
        initial_water_profile = np.array([87.36, 43.74, 52.3, 190, 0.0, 5.09])
        target_water_profile = np.array([134.36, 266.74, 99.30, 94.00, 66.9, 5.09])

        calculated_additions = additions_calculator.calculate_additions(
            initial_water_profile,
            target_water_profile
        )

        expected_additions = {
            'ams': 0.520,
            'calcium_chloride': 0.183,
            'calcium_sulphate': 0.000,
            'dwb': 0.000,
            'magnesium_sulphate': 0.000,
            'sodium_chloride': 0.172,
            'lactic_acid': 0.000
        }

        for key in expected_additions.keys():
            abs_diff = abs(expected_additions[key] - calculated_additions[key])
            self.assertLessEqual(
                abs_diff,
                additions_calculator.TOLERANCE,
                'The addition concentration ' + key + ' deviates too much from the expected value'
            )

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
            'ams': 0.299,
            'calcium_chloride': 0.006,
            'calcium_sulphate': 0.000,
            'dwb': 0.000,
            'lactic_acid': 0.112,
            'magnesium_sulphate': 0.000,
            'sodium_chloride': 0.004
        }

        for key in expected_additions.keys():
            abs_diff = abs(expected_additions[key] - calculated_additions[key])
            self.assertLessEqual(
                abs_diff,
                additions_calculator.TOLERANCE,
                'The addition concentration ' + key + ' deviates too much from the expected value'
            )

    def test_bermondsey_2020_to_achieve_light_hoppy_profile(self):
        # Ca, Cl, SO4, Alkalinity as CO3, Na, Mg
        initial_water_profile = np.array([104, 49.2, 54.0, 184, 33.9, 4.8])
        # I got this profile from the light hoppy profile:
        # https://www.brewersfriend.com/brewing-water-target-profiles/
        # The only change I have made is I modified the Ca, Na, and Mg
        # targets such that they match the initial profile, since the
        # differences are small.
        target_water_profile = np.array([104, 49.2, 150, 0, 33.9, 4.8])

        calculated_additions = additions_calculator.calculate_additions(
            initial_water_profile,
            target_water_profile
        )

        expected_additions = {
            'ams': 0.084,
            'calcium_chloride': 0.000,
            'calcium_sulphate': 0.041,
            'dwb': 0.000,
            'lactic_acid': 0.660,
            'magnesium_sulphate': 0.158,
            'sodium_chloride': 0.000
        }

        for key in expected_additions.keys():
            abs_diff = abs(expected_additions[key] - calculated_additions[key])
            self.assertLessEqual(
                abs_diff,
                additions_calculator.TOLERANCE,
                'The addition concentration ' + key + ' deviates too much from the expected value'
            )


if __name__ == '__main__':
    unittest.main()
