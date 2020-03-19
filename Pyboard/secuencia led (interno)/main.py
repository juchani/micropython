from pyb import LED as l 
from time import sleep as t
led=[l(1),l(2),l(3),l(4)] 
while 1:
    for n in led:
        n.toggle()
        t(1)