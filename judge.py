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
        self.sounds = [load_wav("alert.wav")for i in range(4)]
        self.soundCount=0
        self.sound2 = load_wav("GUNFIRE2.wav")
        for sound in self.sounds:
            sound.get_volume()
        #self.sound2.get_volume()
    def draw(self):
        draw_rectangle(self.x,self.y,self.x+self.width,self.y+self.height)
    def update(self,Character):
        self.x=Character.x+Character.width+30
        self.y=Character.y

    def check(self,note,key):
        x2 = self.x + self.width/2
        if(key==0):
            if (note.mid <= self.x - 30):
               # self.sound2.play()
                return self.miss
            return False
        else:
            if(note.mid>x2+70):
                return False
            if((key== 1 and note.line==1)
               or (key== 2 and note.line==2)
               or (key== 3 and note.line==3)
               or (key== 4 and note.line==4)):
                self.sounds[self.soundCount].play()
                self.soundCount=(self.soundCount+1)%4
                if (note.mid <= self.x - 30or note.mid>x2+30):
                    return self.miss
                elif(note.mid>=self.x and note.mid< x2-10):
                    return self.perfect
                elif (note.mid >= self.x-20 and note.mid < self.x+20):
                    return self.good
                elif (note.mid >= x2-20 and note.mid < x2+20):
                    return self.good
            else: return False
    def __del__(self):

        pass