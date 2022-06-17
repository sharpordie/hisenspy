from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from plyer import irblaster


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="MENU",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                on_release=self.do_it,
            )
        )
        return screen

    def do_it(self, obj):
        carrier = 37810
        pattern = [8900, 4400, 600, 500, 550, 550, 550, 550, 550, 550, 550, 550, 550, 500, 600, 500, 600, 500, 550, 1650, 600, 1650, 550, 1650, 550, 1650, 550, 1650, 550, 1650, 600, 500, 600, 1650, 550, 500, 600, 500, 550, 1650, 600, 500, 550, 1700, 550, 500, 550, 550, 550, 550, 550, 1650, 550, 1700, 500, 550, 550, 1700, 500, 550, 550, 1700, 500, 1700, 500, 1700, 550]
        irblaster.transmit(carrier, pattern)


MainApp().run()
