import pyautogui as pg
from kivymd.app import MDApp
from kivy.lang import Builder

class App(MDApp):
    def build(self):
        self.theme_cls.theme_style='Dark'
        return Builder.load_file("App.kv")
    
    def click_action(self):
        for i in range(int(self.root.ids.scr.numen.text)):
            pg.write(self.root.ids.scr.texten.text)
            pg.press('enter')
    
if __name__ == '__main__':
    App().run()