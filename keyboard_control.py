from djitellopy import tello
import keypress_module as kp
from time import sleep

kp.init()
me = tello.Tello()
me.connect()

print(me.get_battery())

def get_keyboard_input():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if kp.get_key('LEFT'): lr = -speed
    elif kp.get_key('RIGHT'): lr = speed
    
    if kp.get_key('UP'): fb = speed
    elif kp.get_key('DOWN'): fb = -speed

    if kp.get_key('w'): ud = speed
    elif kp.get_key('s'): ud = -speed

    if kp.get_key('a'): yv = -speed
    elif kp.get_key('d'): yv = speed

    if kp.get_key('q'): me.land()
    if kp.get_key('e'): me.takeoff()

    return lr, fb, ud, yv


while True:
    lr, fb, ud, yv  = get_keyboard_input()
    me.send_rc_control(lr, fb, ud, yv )
    sleep(0.05)