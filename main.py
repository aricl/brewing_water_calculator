from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_file('screens/menu.kv')
Builder.load_file('screens/additions_calculator.kv')
Builder.load_file('screens/profile_calculator.kv')


class Menu(Screen):
    pass


class AdditionsCalculator(Screen):
    pass


class ProfileCalculator(Screen):
    pass


screen_manager = ScreenManager()
screen_manager.add_widget(Menu(name='menu'))
screen_manager.add_widget(AdditionsCalculator(name='additions_calculator'))
screen_manager.add_widget(ProfileCalculator(name='profile_calculator'))


class TestApp(App):

    def build(self):
        return screen_manager


if __name__ == '__main__':
    TestApp().run()
