from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dropdownitem import MDDropDownItem
from kivy.properties import ObjectProperty
from router_ui_html import bt_connection_page
from kivy.core.window import Window
from kivy.properties import StringProperty

Window.size = (300, 500)
screen_helper = """

<ScreenManagement>:
    MenuScreen:
        id: screen1
        name: 'menu'
    ProfileScreen:
        id: screen2
        name: 'profile'

<MenuScreen@ListButtonDropdown1>:
    name: 'menu'
    adminpass: adminpass
    Screen
        id: adminpass
        adminp: adminp
        MDTextField:
            id: adminp
            size_hint_x: None
            mode: "rectangle"
            width: "200dp"
            hint_text: 'Admin Password'
            pos_hint: {'center_x': .5, 'center_y': .6}
        ListButtonDropdown1:
            pos_hint: {'center_x': .5, 'center_y': .75}
            text: 'Select Your Router'
            on_release: self.menu.open()
        MDRectangleFlatButton:
            text: 'Login'
            pos_hint: {'center_x':0.5,'center_y':0.45}
            on_press: 
                root.manager.current = root.LogOnRouter()



<ProfileScreen>:
    name: 'profile'

    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title: "Main"
            left_action_items: [["dots-vertical", lambda x: x]]
            right_action_items: [["close-circle-outline", lambda x: app.callback()]]



        MDBottomNavigation:
            panel_color: .2, .2, .2, 1

            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Python'
                icon: 'language-python'
                on_tab_press: 
                    root.navigation_draw()
                    root.manager.transition.direction = 'left'

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


            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'C++'
                icon: 'language-cpp'

                MDLabel:
                    text: 'I programming of C++'
                    halign: 'center'

            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'JS'
                icon: 'language-javascript'

                MDLabel:
                    text: 'JS'
                    halign: 'center'


<UploadScreen>:
    name: 'upload'

    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'menu'
"""


class ScreenManagement(ScreenManager):
    pass


class ListButtonDropdown1(MDDropDownItem):
    print('after string')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        menu_items = [{"icon": "git", "text": "Default"},
                      {"icon": "git", "text": "Router 1"}]
        self.menu = MDDropdownMenu(
            caller=self,
            items=menu_items,
            callback=self.set_item2,
            width_mult=4,
        )

    def set_item2(self, instance):
        self.set_item(instance.text)
        self.menu.dismiss()
        print('happened')
        self.ger = 'siker'
        return self.ger


class MenuScreen(Screen):
    adminpass = ObjectProperty(None)

    def LogOnRouter(self):
        self.check_data_login()
        changescreen = 'profile'
        return changescreen

    def check_data_login(self):
        # print(self.das.set_item2())
        password = self.adminpass.adminp.text
        print(password)


class ProfileScreen(Screen):

    def navigation_draw(self):
        labelin1 = self.ids.label1
        labelin1.text = bt_connection_page()[0]
        labelin2 = self.ids.label2
        labelin2.text = bt_connection_page()[1]
        labelin3 = self.ids.label3
        labelin3.text = bt_connection_page()[2]
        labelin4 = self.ids.label4
        labelin4.text = bt_connection_page()[3]


class UploadScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()

sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))


class DemoApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(screen_helper)

    def build(self):
        return ScreenManagement()


DemoApp().run()
