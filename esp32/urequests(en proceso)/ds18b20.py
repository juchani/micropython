from machine import Pin as p
from time import sleep as t
from urequests import get as rq
import network
import ujson as json
nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('juchani', 'kazeshini')
led=p(2,p.OUT)
for i in range(10):
    h=rq(url='https://api.thingspeak.com/channels/1035427/fields/1.json?api_key=B1YL91D46Z6VDTK6&results=2')
    j=json.loads(h.content)
    h.close()
    temperatura=j["feeds"][1]["field1"]
    print(float(temperatura))

    
    

