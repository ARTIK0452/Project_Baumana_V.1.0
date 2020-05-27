import datetime
import weatherTest
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app	import MDApp, App
from kivymd.theming import ThemableBehavior
from kivymd.uix.picker import MDDatePicker, MDTimePicker, MDThemePicker
from kivymd.uix.behaviors import TouchBehavior
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.label import MDLabel


KV = '''
<ContentNavigationDrawer>:
    ScrollView:
        MDList:

            OneLineListItem:
                text: "Weather"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "weather"

            OneLineListItem:
                text: "History"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "history"

            OneLineListItem:
                text: "About"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "about_me"


Screen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Open Weather"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager
            name: screen_manager

            Screen:
                name: "weather"

                textInput: textInput
                search: search
                cError: cError

                dateTime: dateTime
                cityCountry: cityCountry
                
                MDTextField:
                    id: textInput
                    size_hint: .54, .1
                    pos_hint: {'x': .2, 'y': .67}
                    hint_text: "Введите город для поиска"
                MyButton:
                    id: search
                    size_hint: .54, .08
                    pos_hint: {'x':.2, 'y': .6}
                    text: 'Поиск'
                    
                MDLabel:
                    id: cError
                    size_hint: .54, .08
                    pos_hint: {'x':.46, 'y': .5}
                    text: "*"
                MDGridLayout:
                    adaptive_height: True
                    cols: 2
                    rows: 9
                    pos_hint: {'x':.2,'y': .05}
                    spacing: "30dp"
                    MDLabel:
                        text: "Дата, время"
                    MDLabel:
                        id: dateTime
                        text: "*"
                    MDLabel:
                        text: "Город, cтрана"
                    MDLabel:
                        id: cityCountry
                        text: "*"
                    MDLabel:
                        text: "Актуальная температура"
                    MDLabel:
                        id: CurrentTemperature
                        text: "*"
                    MDLabel:
                        text: "Влажность воздуха"
                    MDLabel:
                        id: AirHumidity
                        text: "*"
                    MDLabel:
                        text: "Давление"
                    MDLabel:
                        id: Pressure
                        text: "*"
                    MDLabel:
                        text: "Облачность"
                    MDLabel:
                        id: Cloudiness
                        text: "*"
                    MDLabel:
                        text: "Осадки"
                    MDLabel:
                        id: Rainfall
                        text: "*"
                    MDLabel:
                        text: "Скорость ветра"
                    MDLabel:
                        id: windSpeed
                        text: "*"
                    MDLabel:
                        text: "Направление ветра"
                    MDLabel:
                        id: windDirection
                        text: "*"
                    
                        
                    
                    
            Screen:
                name: "history"
                MDLabel:
                    text: "Screen 2"
                    halign: "center"

            Screen:
                name: "about_me"
                MDLabel:
                    text: "aa"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''

class MyButton(MDRoundFlatButton):
    def on_release(self, *args):
        print(textInput.text)
        #my = weatherTest.getWeather(city)
        #listWeather = my.geo_location()
        #if listWeather:
        #    self.ids.dateTime.text = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #    print(listWeather)

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)
   
            

TestNavigationDrawer().run()
