import start_state

from pico2d import*

class Ui_top:
    def __init__(self):
        self.width=start_state.scr_width
        self.height=100
    def draw(self):
        draw_rectangle(0,start_state.scr_height-self.height,self.width,start_state.scr_height)

