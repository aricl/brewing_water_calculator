from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class ButtonApp(App):
    def build(self):
        layout = BoxLayout(padding=10)

        additions_from_profile_button = Button(text='Additions From Profile')
        additions_from_profile_button.bind(on_press=self.on_button_press)
        layout.add_widget(additions_from_profile_button)

        profile_from_additions_button = Button(text='Profile From Additions')
        profile_from_additions_button.bind(on_press=self.on_button_press)
        layout.add_widget(profile_from_additions_button)

        return layout

    def on_button_press(self, instance):
        print(instance.text)


if __name__ == '__main__':
    app = ButtonApp()
    app.run()
