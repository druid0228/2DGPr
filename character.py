
from pico2d import *
from judge import*
#state

idle,left_move,right_move=0,1,2

class Character:
    def __init__(self):
        self.image = load_image('test_white.png')
        self.x=0
        self.y=40
        self.width=100
        self.height=100
        self.move_time=0
        self.state=idle
        self.judge=JudgeLine(self)



    def move_right(self):
        if(self.x<800):
            self.state=right_move
            self.move_time=0

    def move_left(self):
        if(self.x>0):
            self.state = left_move
            self.move_time=0

    def update(self):
        if(self.state==idle):
            pass
        elif(self.state==right_move):
            if(self.move_time>30):
                self.state=idle
                self.move_time=0
            else:
                if (self.x < 800):
                    self.x+=1
                    self.move_time+=1
                    self.judge.update(self)
            pass
        elif (self.state == left_move):
            if (self.move_time > 30):
                self.state = idle
                self.move_time = 0
            else:
                if (self.x > 0):
                    self.x -= 1
                    self.move_time += 1
                    self.judge.update(self)

    def draw(self):
        self.image.clip_draw(0,0,10,10,self.x+self.width/2,self.y+self.height/2,self.width,self.height)
        draw_rectangle(self.x,self.y,self.x+self.width,self.y+self.height)
        self.judge.draw()




