from pico2d import *
import start_state

line_one, line_two, line_three, line_four = 1, 2, 3, 4


class Note:
    def __init__(self, line):
        self.x = start_state.scr_width - 50
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
        self.line = line


    def update(self):
        if (self.x > 0):
            self.x -= 1

    def draw(self):
        draw_rectangle(self.x, self.y, self.x + self.width, self.y + self.height)

    def __del__(self):
        pass
