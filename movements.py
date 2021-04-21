from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())
me.takeoff()
# (up/down, front/back, left/right, turn)
me.send_rc_control(0,50,0,0) 
sleep(3)
me.send_rc_control(0,-50,0,0)
sleep(4)
me.send_rc_control(0,0,0,0)
me.land()