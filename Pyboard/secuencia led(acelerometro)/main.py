from pyb import LED as l 
from time import sleep as t
from pyb import Accel
accel = Accel().x
led_i=[l(1),l(2),l(3),l(4)]
def x():
    x=int((int(accel())+21)/14)
    print(x)
    return x
while 1:
    for h in led_i:
        h.off()
    led_i[x()].on()
    t(0.2)