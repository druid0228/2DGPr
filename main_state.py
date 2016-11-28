
from pico2d import*

import game_framework
import title_state
import random
from character import*
from UI_top import*
from note import*

name = "MainState"

grass = None
font = None
combofont=None

time=0
score_perfect=0
score_good=0
score_miss=0
key=0
combo=0
maxCombo=0


frame_time=0.0
current_time = 0.0


def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        self.frame=0

    def draw(self):
        #self.image.draw(400, 30)
        self.image.clip_draw_to_origin(self.frame, 0, 800 - self.frame, 62, 0, 0)
        self.image.clip_draw_to_origin(0, 0, self.frame, 62, 800 - self.frame, 0)
    def update(self):
        self.frame=(self.frame+1)%801

class BackGround:
    def __init__(self):
        self.image=load_image('back.png')
        self.frame=0

    def draw(self):
        self.image.clip_draw_to_origin(self.frame,0,1000-self.frame,600,0,30)
        self.image.clip_draw_to_origin(0,0,self.frame,600,1000-self.frame,30)
    def update(self):
        self.frame=(self.frame+1)%1001

def enter():
    global grass,character,ui_top,notes,time,bgm
    grass=Grass()
    character = Character()
    ui_top=Ui_top()
    notes=[]
    time=0
    bgm=load_music("Praystation.mp3")
    bgm.get_volume()
    bgm.play()
    global font
    font=load_font("ENCR10B.TTF",20)
    global combofont
    combofont = load_font("ENCR10B.TTF", 60)
    global background
    background=BackGround()
    #f=open('pa.txt','rb')
    #mp_list=f.readlines()
    #f.close()
    #for mpl in mp_list:
    #    print(mpl)



def exit():
    global grass,character,ui_top,notes,bgm,font,background
    bgm.stop()
    del(bgm)
    del(grass)
    del(character)
    del(ui_top)
    del(notes)
    del(font)
    del(background)


def pause():
    pass


def resume():
    pass


def handle_events():
    events=get_events()
    global notes
    global key
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            game_framework.change_state(title_state)
            #tmp_move
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            character.move_left()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            character.move_right()
            #tmp_append
        elif event.type == SDL_KEYDOWN and event.key == SDLK_m:
            notes.append(Note(1))
            notes.append(Note(4))
        elif event.type == SDL_KEYDOWN and event.key == SDLK_n:
            notes.append(Note(2))
            notes.append(Note(3))
            #tmp_key
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            key=1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_f:
            key=2
        elif event.type == SDL_KEYDOWN and event.key == SDLK_j:
            key=3
        elif event.type == SDL_KEYDOWN and event.key == SDLK_k:
            key=4

Perfect,good,miss=1,2,3
def update():
    global time
    global score_perfect,score_good,score_miss
    global key
    global frame_time
    global background,grass
    global combo,maxCombo
    frame_time=get_frame_time()
    time += 1
    grass.update()
    if time % 4 == 0:
        background.update()

    character.update(frame_time)


    if time%100 == 0:
        notes.append(Note(random.randint(1,4)))
        #notes.append(Note(random.randint(1,4)))
        
        #notes.append(Note(1))
        #notes.append(Note(3))
    for note in notes:
            #Pass
        if(character.judge.check(note,key)!=False):
            #Score
            if (character.judge.check(note,key) == Perfect):
                score_perfect+=1
                combo+=1
                maxCombo=max(maxCombo,combo)
                print('perfect')
                note.sound(0)
            elif (character.judge.check(note,key) == good):
                score_good+=1
                combo += 1
                maxCombo = max(maxCombo, combo)
                print('good')
                note.sound(0)
            elif (character.judge.check(note,key) == miss):
                score_miss+=1
                combo=0
                print('miss')
                note.sound(0)
            #notes.remove(note)


    for note in notes:
        note.update()
    key=0

def draw():
    global font
    clear_canvas()
    background.draw()
    ui_top.draw()
    grass.draw()
    for note in notes:
        note.draw()

    character.draw()
    ui_top.draw()
    draw_time(700,500)

    combofont.draw(60,170,"%d"%(combo),(100,200,255))
    combofont.draw(100, 550, "MaxCombo %d" % (maxCombo), (100, 0, 255))
    update_canvas()


def draw_time(x,y):
    global font
    font.draw(x,y,"%f"%(get_time()),(0,0,0))





