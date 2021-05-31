from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang.builder import Builder
from views import additions_calculator_helpers
import numpy as np
from profile_calculator import calculate_profile


class AdditionsCalculator(MDApp):
    def create(self):
        screen = Screen()

        self.widgets = []
        for helper in additions_calculator_helpers.helpers:
            self.widgets.append(Builder.load_string(helper))
        for widget in self.widgets:
            screen.add_widget(widget)

        button = MDRectangleFlatButton(
            text='Enter',
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            on_release=self.show_data)
        screen.add_widget(button)

        return screen

    def show_data(self, obj):
        balanced_water_profile = np.array([
            80.0,
            75,
            80,
            100,
            25,
            5
        ])
        additions = [float(widget.text) if widget.text else 0 for widget in self.widgets]
        calculated_profile = calculate_profile(
            balanced_water_profile,
            {
                'ams': additions[0],
                'calcium_chloride': additions[1],
                'calcium_sulphate': additions[2],
                'dwb': additions[3],
                'magnesium_sulphate': additions[4],
                'sodium_chloride': additions[5],
                'lactic_acid': additions[6],
            }
        )

        output_string = ''
        output_string += 'Ca: ' + str(int(calculated_profile[0])) + '\n'
        output_string += 'Cl: ' + str(int(calculated_profile[1])) + '\n'
        output_string += 'SO4: ' + str(int(calculated_profile[2])) + '\n'
        output_string += 'Alkalinity: ' + str(int(calculated_profile[3])) + '\n'
        output_string += 'Na: ' + str(int(calculated_profile[4])) + '\n'
        output_string += 'Mg: ' + str(int(calculated_profile[5])) + '\n'

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