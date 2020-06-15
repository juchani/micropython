from machine import Pin as p
from time import sleep as t
from urequests import get as rq
import network
import ujson as json
nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('juchani', 'kazeshini')
led=p(2,p.OUT,value=1)
for i in range(10):
    h=rq(url='https://maker.ifttt.com/trigger/hhh/with/key/cilbQn9_ISfxSloSJd2qe0asE8FjH4jvO_ejnBp1WHI?value1={}'.format(i))
    print(h)
    h=None
    led.on()
    t(0.03)
    led.off()
    t(0.03)
    