from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('rightCha.png')
hand = load_image('hand_arrow.png')


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_q: # q누르면 꺼짐
                running = False
    pass

handX, handY = 100,100



speed = 10 # 스피드 설정

def goToHand():
    global x,y,handX,handY,chaDir,drawHand
    print(' 캐릭터가 손 따라가는것~~ ')

    if(x < handX):
        chaDir = 1
        x+=speed
    elif(x>handX):
        chaDir = -1
        x-=speed
    elif(x==handX):
        chaDir = 1

    if(y < handY):
        y+=speed
    elif(y>handY):
        y-=speed
    elif (y == handY):
        chaDir = 1

    if(abs(x-handX) <= 5 and abs(y-handY) <= 10):
        handX = random.randint(0, 1200)
        handY = random.randint(0, 1000)

    pass

def drawCha():
    global frame,handX,handY,x,y,character,hand,chaDir
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    hand.clip_draw(0, 0, 50, 52, handX, handY)

    if(chaDir == 1):
        character = load_image('rightCha.png')
    elif(chaDir == -1):
        character = load_image('leftCha.png')

    character.clip_draw(frame * 100, 0, 100, 100, x, y, 80, 80)

    update_canvas()
    frame = (frame + 1) % 2


running = True

chaDir = 1 # 오른쪽이면 1, 왼쪽이면 -1로
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2

frame = 0
hide_cursor()

while running:
    goToHand()
    drawCha() # 그리는 함수 하나로 빼기

    print(abs(x-handX),abs(y-handY))
    print(x,y)

    handle_events()
    delay(0.03)

close_canvas()




