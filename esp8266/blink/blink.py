import machine, time

def toggle(p):
    p.value(not p.value())

pin = machine.Pin(12, machine.Pin.OUT)
while True:
    toggle(pin)
    time.sleep_ms(500)
    
