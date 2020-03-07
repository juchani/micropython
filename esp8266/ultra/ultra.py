import machine
import time
def ultra():
  trig=machine.Pin(2, machine.Pin.OUT)
  trig.off()
  time.sleep_us(2)
  trig.on()
  time.sleep_us(10)
  trig.off()
  echo=machine.Pin(4, machine.Pin.IN)
  while echo.value() == 0:
    pass
  t1 = time.ticks_us()
  while echo.value() == 1:
    pass
  t2 = time.ticks_us()
  cm = (t2 - t1) / 58.0
  return cm
while 1:
  print(int(ultra())+" CM")
  time.sleep_ms(500)
