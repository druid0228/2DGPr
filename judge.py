from character import*
from pico2d import*

class JudgeLine:
    def __init__(self,Character):
        self.x=Character.x+Character.width+30
        self.y=Character.y
        self.width=100
        self.height=400
        self.perfect=1
        self.good=2
        self.miss=3
    def draw(self):
        draw_rectangle(self.x,self.y,self.x+self.width,self.y+self.height)
    def update(self,Character):
        self.x=Character.x+Character.width+30
        self.y=Character.y

    def check(self,note,key):
        x2 = self.x + 100
        if(key==0):
            if (note.x <= self.x - 30):
                return self.miss
            return False
        else:
            if(note.x>x2+70):
                return False
            if((key== 1 and note.line==1)
               or (key== 2 and note.line==2)
               or (key== 3 and note.line==3)
               or (key== 4 and note.line==4)):
                if (note.x <= self.x - 30or note.x>x2+30):
                    return self.miss
                elif(note.x>=self.x and note.x< x2-10):
                    return self.perfect
                elif (note.x >= self.x-20 and note.x < self.x+20):
                    return self.good
                elif (note.x >= x2-20 and note.x < x2+20):
                    return self.good
            else: return False
    def __del__(self):

        pass