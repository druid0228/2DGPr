from pico2d import *

class Monster:
    def __init__(self):
        self.image = load_image('test_white.png')
        self.x=0.0
        self.y=40.0
        self.width=100
        self.height=100
        self.move_time=0



    def update(self,frame_time):
            if (self.x > 0):
                self.x+=frame_time*(-300)
                self.move_time+=1
                self.judge.update(self)


    def draw(self):
        self.image.clip_draw(0,0,10,10,self.x+self.width/2,self.y+self.height/2,self.width,self.height)
        draw_rectangle(self.x,self.y,self.x+self.width,self.y+self.height)
