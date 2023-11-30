from kivymd.app import MDApp
from kivy.lang import Builder

class picaApp(MDApp):
    def build(self):
        self.appKv='''
MDScreen:
    MDLabel:
        text:'Hello World'
        halign: 'center'
'''

        AppScreen = Builder.load_string(self.appKv)
        return AppScreen

picaApp().run()