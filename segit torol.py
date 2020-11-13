from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.chip import MDChip
from kivy.core.window import Window
Window.size = (400, 600)
from kivymd.uix.menu import MDDropdownMenu
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder

screen_helper = """
<WindowManager>
    Container:
        id: scr_1
        name: 'container'
    Detail:
        id: scr_2
        name: 'detail'

    Admin:
        id: scr_3
        name: 'admin'
    EditArticle:
        id: scr_4
        name: 'edit-article'
        var: scr_3.my_string # <---------

    ResultSearch:
        id: scr_5
        name: 'result-search'
    UserSettings:
        id: scr_6
        name: 'settings'

<Admin>:
    BoxLayout:
        id: boxlayout_1
        orientation: 'vertical'

        MDToolbar:
            pos_hint: {'top': 1}
            title: 'Admin Blog'
            left_action_items: [["arrow-left", lambda x: app.callback()]]

        ScrollView:
            MDStackLayout:
                adaptive_height: True
                padding: 10
                spacing: dp(5)
                id: box

<EditArticle>
    MDToolbar:
        title: 'Admin Blog'
    MDLabel:
        text: str(root.var)
    MDRaisedButton:
        text: 'click me to see a variable in console'
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: root.edit(root)

"""
class WindowManager(ScreenManager):
    pass



class Admin(Screen):

    dialog_get_article = None

    my_string = StringProperty() # My string

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_article(self, instance,*args):
        self.dialog_get_article = MDDialog(
            title="Click the EDIT",
            buttons=[
                MDFlatButton(
                    text="EDIT",
                    on_release = self.edit_article
                ),
            ],
        )
        self.dialog_get_article.open()

    def edit_article(self, instance):

        self.my_string = 'some text' # set value
        App.get_running_app().window_manager.current = 'edit-article'
        self.dialog_get_article.dismiss()

    def on_enter(self, *args):
        data = [
            {'id': 1, 'title': 'Arcicle 1', 'body': 'body of Article 1'},
            {'id': 2, 'title': 'Arcicle 2', 'body': 'body of Article 2'},
            {'id': 3, 'title': 'Arcicle 3', 'body': 'body of Article 3'}
        ]
        for x in data:
            chip = BlogChip(id=x.get('id'), title=x.get('title'), body=x.get('body'))
            self.ids.box.add_widget(chip)

class EditArticle(Screen):

    var = StringProperty()

    def edit(self, instance):
        self.var = self.manager.ids.scr_3.my_string
        print(self.var)

class UserSettings(Screen):
    pass

class BlogChip(MDChip):


    id = NumericProperty()
    title = StringProperty()
    body = StringProperty()

class Container(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.create_cards)

    def create_cards(self, i):
        pass

class App(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(screen_helper)

    def callback(self):
        self.window_manager.current = 'container'

    def build(self):
        self.theme_cls.primary_palette = 'Indigo'
        self.window_manager = WindowManager()
        return self.window_manager

App().run()