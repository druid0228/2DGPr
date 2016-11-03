
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
time=0
score_perfect=0
score_good=0
score_miss=0
key=0


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

    def draw(self):
        self.image.draw(400, 30)


def enter():
    global grass,character,ui_top,notes,time,bgm
    grass=Grass()
    character = Character()
    ui_top=Ui_top()
    notes=[]
    time=0
    #bgm=load_music("Praystation.mp3")
    #bgm.get_volume()
    #bgm.play()
    #f=open('pa.txt','rb')
    #mp_list=f.readlines()
    #f.close()
    #for mpl in mp_list:
    #    print(mpl)



def exit():
    global grass,character,ui_top,notes
    del(grass)
    del(character)
    del(ui_top)
    del(notes)


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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            character.move_left()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            character.move_right()
            #tmp_append
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            notes.append(Note(1))
            notes.append(Note(4))
        elif event.type == SDL_KEYDOWN and event.key == SDLK_e:
            notes.append(Note(2))
            notes.append(Note(3))
            #tmp_key
        elif event.type == SDL_KEYDOWN and event.key == SDLK_z:
            key=1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_x:
            key=2
        elif event.type == SDL_KEYDOWN and event.key == SDLK_c:
            key=3
        elif event.type == SDL_KEYDOWN and event.key == SDLK_v:
            key=4

Perfect,good,miss=1,2,3
def update():
    global time
    global score_perfect,score_good,score_miss
    global key
    global frame_time
    frame_time=get_frame_time()
    character.update(frame_time)
    time+=1
    if time%300 == 0:

        #notes.append(Note(random.randint(1,4)))
        notes.append(Note(1))
    for note in notes:
            #Pass
        if(character.judge.check(note,key)==False):
            continue
            #Score
        else:
            if (character.judge.check(note,key) == Perfect):
                score_perfect+=1
                print('perfect')
            elif (character.judge.check(note,key) == good):
                score_good+=1
                print('good')
            elif (character.judge.check(note,key) == miss):
                score_miss+=1
                print('miss')
            notes.remove(note)


    for note in notes:
        note.update()
    key=0

def draw():
    clear_canvas()
    ui_top.draw()
    grass.draw()
    for note in notes:
        note.draw()

    character.draw()
    ui_top.draw()

    update_canvas()






