from machine import Pin as p
from time import sleep as t
import network
# enable station interface and connect to WiFi access point
nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('juchani', 'kazeshini')
led=p(2,p.OUT)

led.on()
t(1)
led.off()
t(1)
