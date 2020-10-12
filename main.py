from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_file('screens/menu.kv')
Builder.load_file('screens/additions_calculator.kv')
Builder.load_file('screens/profile_calculator.kv')


# Declare both screens
class Menu(Screen):
    pass


class AdditionsCalculator(Screen):
    pass


class ProfileCalculator(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(Menu(name='menu'))
sm.add_widget(AdditionsCalculator(name='additions_calculator'))
sm.add_widget(ProfileCalculator(name='profile_calculator'))


class TestApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()
