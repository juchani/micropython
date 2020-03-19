from pyb import LED as l 
from time import sleep as t
led=l(1) 
while 1:
    led.toggle()
    t(1)