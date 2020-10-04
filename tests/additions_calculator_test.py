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
            'ams': 0.8648391103352605,
            'calcium_chloride': 0.0011139165073896446,
            'calcium_sulphate': 0.0035957554672154195,
            'dwb': 0.6061061694861456,
            'magnesium_sulphate': 0.0002575288068418974,
            'sodium_chloride': 2.7145175866105684e-05,
            'lactic_acid': 3.2903174043822476e-13
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
            'ams': 2.8715662680231717e-12,
            'calcium_chloride': 0.10912928826582009,
            'calcium_sulphate': 0.07481680938665661,
            'dwb': 2.7627992916348135e-13,
            'magnesium_sulphate': 5.44241008550406e-12,
            'sodium_chloride': 9.821551822047647e-16,
            'lactic_acid': 0.6112188819347667
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
            'ams': 0.5199770139176254,
            'calcium_chloride': 0.18272541124061567,
            'calcium_sulphate': 5.353747450405045e-12,
            'dwb': 5.0680350679175664e-14,
            'magnesium_sulphate': 0.0005179759787675492,
            'sodium_chloride': 0.1718213726401725,
            'lactic_acid': 0.0
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
            'ams': 0.29915894674470517,
            'calcium_chloride': 0.0064505987224074916,
            'calcium_sulphate': 2.5857922549169753e-09,
            'dwb': 1.7393391168183756e-09,
            'lactic_acid': 0.11218802678559774,
            'magnesium_sulphate': 6.13461269265889e-05,
            'sodium_chloride': 0.003932229239953924
        }

        self.assertEqual(expected_additions, calculated_additions)

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
            'ams': 0.0843005857190059,
            'calcium_chloride': 1.6520551798669604e-09,
            'calcium_sulphate': 0.040956599353334774,
            'dwb': 0.0,
            'lactic_acid': 0.6604197826912657,
            'magnesium_sulphate': 0.15809240755380205,
            'sodium_chloride': 0.0
        }

        self.assertEqual(expected_additions, calculated_additions)


if __name__ == '__main__':
    unittest.main()
