# play in PyGame Zero mode
import random

alien = Actor('alien')
startPoint = (100,400)
alien.pos = startPoint

hurdle = Actor('cat1')
hurdle.pos = 100,100
alien.center

box = Rect((20,20),(100,100))

#키보드 사이즈
WIDTH = 500
HEIGHT = 400

#한번에 얼마나 움직여야하는지(에일리언 사이즈)
xStep = alien.right-alien.left
yStep = alien.bottom - alien.top

speed = 1

success = False

def draw():
    global success
    screen.clear()
    alien.draw()
    if not success :
        hurdle.draw()

    screen.draw.rect(box,(100,100,100))

def update():
    global success
    print(success)
    keyDown()
    hurdle.right+= 2 * speed
    alienPosUpdate()
    speedUpdate()

    if hurdle.colliderect(alien):
        print("colide")
        alien.pos = startPoint


    if alien.top <=0:
        print("Success")
        success =True
        alien.pos = startPoint

def speedUpdate():

    if hurdle.right >=WIDTH or hurdle.left<=0:
        speed = random.random()
        hurdle.left = 0


def alienPosUpdate():

    if alien.right >= WIDTH:
        alien.left =0

    elif alien.left <=0 :
        alien.right =WIDTH

def keyDown():

    if keyboard.left:
        print("dfdfdf")
        alien.x -= 3
    elif keyboard.right:
        alien.x += 3

    elif keyboard.up:
        print("up")
        alien.y-=10


'''
def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()
        #alien.image = 'alien_hurt'
    else:
        print("You missed me!")


def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_interval(set_alien_normal, 0.5)


def set_alien_normal():
    alien.image = 'alien'

'''
# Write your code here :-)
