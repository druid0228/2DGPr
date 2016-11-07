from pico2d import*

def draw_time(x,y):
    global fontt
    fontt.draw(x,y,"%f"%(get_time()),(0,0,0))

def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def handle_events():
    events=get_events()
    global notes
    global key
    for event in events:
        if event.type==SDL_QUIT:
            quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_z:
            key=1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_x:
            key=2
        elif event.type == SDL_KEYDOWN and event.key == SDLK_c:
            key=3
        elif event.type == SDL_KEYDOWN and event.key == SDLK_v:
            key=4

def update():
   pass

open_canvas()
image = load_image('wall.jpg')
fontt= load_font("ENCR10B.TTF",40)

while True:
    clear_canvas()
    #image.draw(0,0,800,600)
    draw_time(400,500)
    update_canvas()
