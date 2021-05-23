from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang.builder import Builder
import helpers
import numpy as np

from profile_calculator import calculate_profile


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.calcium_concentration = Builder.load_string(helpers.calcium_concentration_definition)
        self.chloride_concentration = Builder.load_string(helpers.chloride_concentration_definition)
        self.sulphate_concentration = Builder.load_string(helpers.sulphate_concentration_definition)
        self.alkalinity_as_carbonate_concentration = Builder.load_string(helpers.alkalinity_as_carbonate_concentration_definition)
        self.sodium_concentration = Builder.load_string(helpers.sodium_concentration_definition)
        self.magnesium_concentration = Builder.load_string(helpers.magnesium_concentration_definition)
        screen.add_widget(self.calcium_concentration)
        screen.add_widget(self.chloride_concentration)
        screen.add_widget(self.sulphate_concentration)
        screen.add_widget(self.alkalinity_as_carbonate_concentration)
        screen.add_widget(self.sodium_concentration)
        screen.add_widget(self.magnesium_concentration)
        button = MDRectangleFlatButton(
            text='Enter',
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            on_release=self.show_data)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        if self.calcium_concentration.text is "":
            output_string = 'Please enter a calcium concentration'

        water_profile = np.array([
            float(self.calcium_concentration.text),
            float(self.chloride_concentration.text),
            float(self.sulphate_concentration.text),
            float(self.alkalinity_as_carbonate_concentration.text),
            float(self.sodium_concentration.text),
            float(self.magnesium_concentration.text)
        ])
        calculated_profile = calculate_profile(
            water_profile,
            {
                'ams': 1,
                'calcium_chloride': 0,
                'calcium_sulphate': 0,
                'dwb': 0,
                'magnesium_sulphate': 0,
                'sodium_chloride': 1,
                'lactic_acid': 0,
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
            title='Titular Title',
            size_hint=(0.7, 1),
            buttons=[close_button, more_button])
        self.dialog.open(self)

    def close_dialog(self, obj):
        self.dialog.dismiss(self)


DemoApp().run()
