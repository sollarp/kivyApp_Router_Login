from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dropdownitem import MDDropDownItem
from kivy.properties import ObjectProperty
from Router_UI_Scrape.BT_Hub5_ConnPage import Hub_5
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


screen_helper = """
<ScreenManagement>:
    MenuScreen:
        id: screen1
        name: 'menu'
    ProfileScreen:
        id: screen2
        name: 'profile'
    UploadScreen:
        id: screen3
        name: 'upload'

<MenuScreen>:
    name: 'menu'
    adminpass: adminpass
    Screen
        id: adminpass
        adminp: adminp
        list: list
        MDTextField:
            id: adminp
            size_hint_x: None
            mode: "rectangle"
            width: "200dp"
            hint_text: 'Admin Password'
            pos_hint: {'center_x': .5, 'center_y': .6}
        ListButtonDropdown1:
            id: list
            pos_hint: {'center_x': .5, 'center_y': .75}
            text: 'Select Your Router'
            on_release: self.menu.open()
        MDRectangleFlatButton:
            text: 'Login'
            pos_hint: {'center_x':0.5,'center_y':0.45}
            on_press: 
                root.manager.current = root.check_data_login()



<ProfileScreen>:
    name: 'profile'

    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title: "Main"
            left_action_items: [["arrow-left-bold-circle-outline", lambda x: root.manager.change_screen("menu")]]
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
                                text: ''
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


hub5 = Hub_5()
## Getting dropdown item from ListButtonDropdown1 class
class InstanceHolder():
    test_instance = None

    def set_instance(self, instance):
        self.test_instance = instance


dummy_instance = InstanceHolder()


class ScreenManagement(ScreenManager):
    def change_screen(self, screen):
        # the same as in .kv: app.root.current = screen
        self.current = screen


class ListButtonDropdown1(MDDropDownItem):
    instance_text = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        menu_items = [{"icon": "git", "text": "Default"},
                      {"icon": "git", "text": "Router 1"}]
        self.menu = MDDropdownMenu(
            caller=self,
            items=menu_items,
            callback=self.set_item_c,
            width_mult=4,
        )
        dummy_instance.set_instance(self)

    def set_item_c(self, instance):
        self.set_item(instance.text)
        self.menu.dismiss()
        self.instance_text = instance.text

    # def get_instance_text(self):
    # return self.instance_text


class MenuScreen(Screen, MDApp):
    adminpass = ObjectProperty(None)
    dialog = None
    ## log into Router
    def check_data_login(self):

        password = self.adminpass.adminp.text
        #selecteditem = self.adminpass.list.current_item
        hub5.get_password(admin_pass=password)
        # print(password)
        # print(selecteditem)

        # hub5.bt_connection_page()
        incorrect_pass = hub5.admin_login()
        self.dialog = incorrect_pass
        if not self.dialog:
            self.dialog = MDDialog(
                title="ERROR",
                text="Incorrect password or no connection to router",
                buttons=[
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color),
                ],
            )
            self.dialog.open()
        else:
            return 'profile'
    ## change screen to profile screen
    def test_pass(self):
        return 'profile'


class ProfileScreen(Screen):
    ## calling data to display on screen change
    def on_enter(self, *args):
        self.navigation_draw()
    ## presenting scrapped data from router connection page into kivy label
    def navigation_draw(self):
        labels = hub5.bt_connection_page()
        try:
            labelin1 = self.ids.label1
            labelin1.text = labels[0]
            labelin2 = self.ids.label2
            labelin2.text = labels[1]
            labelin3 = self.ids.label3
            labelin3.text = labels[2]
            labelin4 = self.ids.label4
            labelin4.text = labels[3]
        except TypeError as e:
            if hub5.bt_connection_page() is None:
                print("device not connected to network")
            else:
                print("router not supported")

    ## change screen to upload screen
    def set_screen(self):
        print(MDApp.get_running_app())
        ScreenManager.current = "upload"


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
        Builder.load_string(screen_helper)

    def build(self):
        return ScreenManagement()


if __name__ == '__main__':
    DemoApp().run()
