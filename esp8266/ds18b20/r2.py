from machine import Pin
import time, ds18x20,onewire
s = onewire.OneWire(Pin(12))
ds = ds18x20.DS18X20(s)
roms = ds.scan()
while 1:
    ds.convert_temp()
    time.sleep(1)
    for rom in roms:
        a=ds.read_temp(rom)
    print(str(a)+' P')
