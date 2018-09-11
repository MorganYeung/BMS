# Pi Dorm GUI
import datetime
import math
import random
import sys
import time
import datetime
from datetime import date

import kivy
#import matplotlib as mp1
#mp1.use('Agg')
#import matplotlib.pyplot as plt
from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.window import Window
#from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from openpyxl import Workbook, load_workbook


# Screen Configuration
Config.read('config.ini')
Config.set('graphics', 'width', 1920)
Config.set('graphics', 'height', 1080)
Config.set('graphics', 'fullscreen', 0)
Config.set('graphics', 'borderless',0)
Config.set('kivy','keyboard_mode', 'dock')
Config.write()

class MenuScreen(Screen):
    def weather_btn(self):
        print("The weather is awesome!")

    def clock_btn(self):
        print("The time is ... about time you got a watch!")

    def alarm_btn(self):
        print("Wake up at 8am? Are you kidding?")

    def calendar_btn(self):
        print("I don't know what day it is...")

    def timer_btn(self):
        print("Lets boil some eggs!")

    def preferences_btn(self):
        print("Lets change something!")

    def desktop_btn(self):
        print("We should get out of here...")

    def exit(self):
        sys.exit()

class ClockScreen(Screen):

    current_time = StringProperty()
    current_date = StringProperty()
    current_ampm = StringProperty()
    KivyClock.schedule_interval(clock.update, 1.0)

    def update(self, dt):
        self.current_time = strftime('%H:%M')
        self.current_date = strftime('%d %b %Y')

    def exit(self):
        sys.exit()

class WeatherScreen(Screen):
    pass
class NewsScreen(Screen):
    pass
class LEDScreen(Screen):
    pass
class FanScreen(Screen):
    pass
#Popup classes are empty, see lat.kv
class SomePop(Popup):
    pass


class Manager(ScreenManager):
    MenuScreen = ObjectProperty(None)
    ClockScreen = ObjectProperty(None)
    WeatherScreen = ObjectProperty(None)
    NewsScreen = ObjectProperty(None)
    LEDScreen = ObjectProperty(None)
    FanScreen = ObjectProperty(None)

class PiDormApp(App):

    def build(self):
        m = Manager()
        return m

if __name__ == '__main__':
    PiDormApp().run()
