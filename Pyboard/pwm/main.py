import pyb
from time import sleep_ms as t
l=pyb.LED(4)
adc=pyb.ADC('A0')
def c(x,in_min,in_max,out_min,out_max):
    f=(x-in_min)*(out_max-out_min)/(in_max-in_min)+out_min
    return int(f)
    

while 1:
    conv=c(adc.read(),0,4095,255,0)
    l.intensity(conv)
    print(conv)
    
    t(50)