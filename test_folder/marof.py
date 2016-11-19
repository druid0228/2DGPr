from pico2d import *
import start_state

line_one, line_two, line_three, line_four = 1, 2, 3, 4


class Maro:
    def __init__(self, line):
        self.x = start_state.scr_width - 50
        self.image=load_image("note.png")

        if (line == line_one):
            self.y = start_state.scr_height - 300
        elif (line == line_two):
            self.y = start_state.scr_height - 400
        elif (line == line_three):
            self.y = start_state.scr_height - 500
        elif (line == line_four):
            self.y = start_state.scr_height - 600
        self.width = 100
        self.height = 100
        self.swidth = 100
        self.cheight = 100
        self.dwidth = 100
        self.dheight = 100
        self.line = line
        self.mid=self.x+self.width/2
        self.mad=10
        self.aa=29


    def update(self):
        if (self.x > 0):
            self.x -= 1
            self.mid-=1
        self.mad+=1
        self.aa-=2


    def draw(self):
        draw_rectangle(self.x, self.y, self.x + self.width, self.y + self.height)
        self.image.clip_draw(0,0,64,64,self.x+50,self.y+50)

    def __del__(self):
        del(self.image)
        pass