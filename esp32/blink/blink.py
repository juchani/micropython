from machine import Pin as p
from time import sleep as t
led=p(2,p.OUT)
while 1:
    led.on()
    t(0.3)
    led.off()
    t(0.3)
    
