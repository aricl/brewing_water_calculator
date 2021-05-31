from kivymd.app import MDApp
from views.additions_calculator import AdditionsCalculator


class BrewingWaterCalculatorApp(MDApp):
    def build(self):
        additions_calculator = AdditionsCalculator()

        return additions_calculator.create()


BrewingWaterCalculatorApp().run()
