
from pico2d import *
from judge import*
#state

idle,left_move,right_move=0,1,2


class Character:
    def __init__(self):
        self.image = load_image('프론.png')
        self.x=0.0
        self.y=40.0
        self.width=100
        self.height=100
        self.move_time=0
        self.sprite_x=0
        self.sprite_y=0
        self.state=idle
        self.judge=JudgeLine(self)
        self.sprite_time=0



    def move_right(self):
        if(self.x<800):
            self.state=right_move
            self.move_time=0

    def move_left(self):
        if(self.x>0):
            self.state = left_move
            self.move_time=0

    def update(self,frame_time):
        self.sprite_time+=frame_time

        if(self.state==idle):
            if(self.sprite_time>1/10.0):
                self.sprite_x=(self.sprite_x+1)%6
                self.sprite_time=0
        elif(self.state==right_move):
            if(self.move_time>30):
                self.state=idle
                self.move_time=0
            else:
                if (self.x < 800):
                    self.x+=frame_time*300
                    self.move_time+=1
                    self.judge.update(self)
                    if (self.sprite_time > 1 / 10.0):
                        self.sprite_x = (self.sprite_x + 1) % 6
                        self.sprite_time = 0
            pass
        elif (self.state == left_move):
            if (self.move_time > 30):
                self.state = idle
                self.move_time = 0
            else:
                if (self.x > 0):
                    self.x -= frame_time*300
                    self.move_time += 1
                    self.judge.update(self)
                    if (self.sprite_time > 1 / 10.0):
                        self.sprite_x = (self.sprite_x + 1) % 6
                        self.sprite_time = 0

    def draw(self):
        if(True):
            self.image.clip_draw(self.sprite_x*102,2527-(170*1),102,170,self.x+self.width/2,self.y+self.height/2,self.width,self.height)
        draw_rectangle(self.x,self.y,self.x+self.width,self.y+self.height)
        self.judge.draw()




