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
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_q: # q누르면 꺼짐
                running = False
    pass

handX, handY = 30,30
isHand = True
def drawHand():
    print(' #손 랜덤으로 불러오는 것~~ ')
    handX = random.randint(0,1200)
    handY = random.randint(0,1000)

    hand.clip_draw(0,0,50,52,handX,handY)
    pass

def goToHand():
    #
    print(' 캐릭터가 손 따라가는것~~ ')
    pass

def checkRL():
    print(' # 좌우 확인하는 것~~  ')

    # 새로 생긴 손이 기존 위치보다 왼쪽이면 left = True
    
    # 새로 생긴 손이 기존 위치보다 오른쪽이면 right = True 해주기


running = True
right= True
left= False # 좌우..
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if(isHand):
        drawHand()

    if(right):
        character = load_image('rightCha.png')
    elif(left):
        character = load_image('leftCha.png')

        
    character.clip_draw(frame * 100, 0, 100, 100, x, y, 80, 80)
    update_canvas()
    frame = (frame + 1) % 2
    delay(0.02)

    handle_events()

close_canvas()




