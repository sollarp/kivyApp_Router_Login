from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from Router_UI_Scrape.BT_Hub5_ConnPage import bt_connection_page
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

Window.size = (300, 500)

screen_helper = """
BoxLayout:

    orientation: "vertical"

    MDToolbar:
        title: "Main"
        left_action_items: [["dots-vertical", lambda x: x]]
        right_action_items: [["close-circle-outline", lambda x: app.callback()]]
        elevation: 10

    Screen:
        id: screen1
        name: 'screen1'

        MDCard:
            orientation: "vertical"
            padding: "8dp"
            size_hint: 0.80, 0.50
            size: "210dp", "380dp"
            pos_hint: {"center_x": .5, "center_y": .4}
            BoxLayout:
                col: 1
                orientation: 'horizontal'
                Label:
                    text: 'Connection Information'
                    id: con_info
                    color: 1,0,1,1
                    font_size: 15
            MDSeparator:
                height: "4dp"

            BoxLayout:
                col: 1
                orientation: 'horizontal'
                Label:
                    id: line_state
                    text: 'Line state:'
                    color: 1,0,1,1
                    font_size: 15


                Label:
                    text: 'bf'
                    id: label1
                    color: 1,0,1,1
                    font_size: 15

            MDSeparator:
                height: "2dp"

            BoxLayout:
                col: 1
                orientation: 'horizontal'


                Label:
                    text: 'Downstream:'
                    id: downstream
                    color: 1,0,1,1
                    font_size: 15
                Label:
                    text: ''
                    id: label2
                    color: 1,0,1,1
                    font_size: 15
            MDSeparator:
                height: "1dp"
            BoxLayout:
                col: 1
                orientation: 'horizontal'
                Label:
                    text: 'Upstream'
                    id: upstream
                    color: 1,0,1,1
                    font_size: 15
                Label:
                    text: ''
                    id: label3
                    color: 1,0,1,1
                    font_size: 15
            MDSeparator:
                height: "1dp"
            BoxLayout:
                col: 1
                orientation: 'horizontal'
                Label:

                    text: 'Connection time:'
                    id: connection_time
                    color: 1,0,1,1
                    font_size: 15
                Label:
                    text: ''
                    id: label4
                    color: 1,0,1,1
                    font_size: 15




    MDBottomAppBar:
        MDToolbar:

            icon: "plus"
            type: "bottom"
            left_action_items: [["menu", lambda x: x]]

            right_action_items: [["settings-outline", lambda x: app.navigation_draw()]]



"""



class StatusScreen(Screen):
    pass
class LoginScreen(Screen):
    pass

class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)

        return screen

    def navigation_draw(self):
        labelin1 = self.root.ids.label1
        labelin1.text = bt_connection_page()[0]
        labelin2 = self.root.ids.label2
        labelin2.text = bt_connection_page()[1]
        labelin3 = self.root.ids.label3
        labelin3.text = bt_connection_page()[2]
        labelin4 = self.root.ids.label4
        labelin4.text = bt_connection_page()[3]


        #print(self.root.ids.label1)
        print("Navigation")

    def set_screen(self):
        print("tatalat2")


DemoApp().run()

