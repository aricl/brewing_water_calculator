from kivymd.app import MDApp
from views.profile_calculator import ProfileCalculator


class BrewingWaterCalculatorApp(MDApp):
    def build(self):
        profile_calculator = ProfileCalculator()

        return profile_calculator.create()


BrewingWaterCalculatorApp().run()
