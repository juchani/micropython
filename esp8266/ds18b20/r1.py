from machine import Pin
import time, ds18x20,onewire
ow = onewire.OneWire(Pin(12)) # create a OneWire bus on GPIO12
#ow.scan() # return a list of devices on the bus
#ow.reset() # reset the bus
#ow.readbyte() # read a byte
#ow.writebyte(0x12) # write a byte on the bus
#ow.select_rom(b'12345678')
ds = ds18x20.DS18X20(ow)
roms = ds.scan()
while 1:
    ds.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        a=ds.read_temp(rom)
        #print(ds.read_temp(rom))
    print(str(a)+' C')
