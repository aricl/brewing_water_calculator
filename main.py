from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang.builder import Builder
import helpers
import numpy as np

from profile_calculator import calculate_profile


class BrewingWaterCalculatorApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__()
        self.lactic_acid = Builder.load_string(helpers.lactic_acid_definition)
        self.sodium_chloride = Builder.load_string(helpers.sodium_chloride_definition)
        self.magnesium_sulphate = Builder.load_string(helpers.magnesium_sulphate_definition)
        self.dwb = Builder.load_string(helpers.dwb_definition)
        self.calcium_sulphate = Builder.load_string(helpers.calcium_sulphate_definition)
        self.calcium_chloride = Builder.load_string(helpers.calcium_chloride_definition)
        self.ams = Builder.load_string(helpers.ams_definition)

    def build(self):
        screen = Screen()
        screen.add_widget(self.ams)
        screen.add_widget(self.calcium_chloride)
        screen.add_widget(self.calcium_sulphate)
        screen.add_widget(self.dwb)
        screen.add_widget(self.magnesium_sulphate)
        screen.add_widget(self.sodium_chloride)
        screen.add_widget(self.lactic_acid)
        button = MDRectangleFlatButton(
            text='Enter',
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            on_release=self.show_data)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        if self.ams.text is "":
            output_string = 'Please enter additions to calculate a water profile'

        balanced_water_profile = np.array([
            80.0,
            75,
            80,
            100,
            25,
            5
        ])
        ams = float(self.ams.text)
        calcium_chloride = float(self.calcium_chloride.text)
        calcium_sulphate = float(self.calcium_sulphate.text)
        dwb = float(self.dwb.text)
        magnesium_sulphate = float(self.magnesium_sulphate.text)
        sodium_chloride = float(self.sodium_chloride.text)
        lactic_acid = float(self.lactic_acid.text)
        calculated_profile = calculate_profile(
            balanced_water_profile,
            {
                'ams': ams,
                'calcium_chloride': calcium_chloride,
                'calcium_sulphate': calcium_sulphate,
                'dwb': dwb,
                'magnesium_sulphate': magnesium_sulphate,
                'sodium_chloride': sodium_chloride,
                'lactic_acid': lactic_acid,
            }
        )

        output_string = ''
        output_string += 'Ca: ' + str(calculated_profile[0]) + '\n'
        output_string += 'Cl: ' + str(calculated_profile[1]) + '\n'
        output_string += 'SO4: ' + str(calculated_profile[2]) + '\n'
        output_string += 'Alkalinity: ' + str(calculated_profile[3]) + '\n'
        output_string += 'Na: ' + str(calculated_profile[4]) + '\n'
        output_string += 'Mg: ' + str(calculated_profile[5]) + '\n'

        close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        more_button = MDFlatButton(text='More')
        self.dialog = MDDialog(
            text=output_string,
            title='Calculated Water Profile',
            size_hint=(0.7, 1),
            buttons=[close_button, more_button])
        self.dialog.open(self)

    def close_dialog(self, obj):
        self.dialog.dismiss(self)


BrewingWaterCalculatorApp().run()
