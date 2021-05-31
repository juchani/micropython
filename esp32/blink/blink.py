import machine
from time import sleep_ms as t

def toggle(p):
    p.value(not p.value())

pin = machine.Pin(2, machine.Pin.OUT)
while True:
    toggle(pin)
    t(500)
    