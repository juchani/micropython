# ejemplo micropython 
# te interesa mas sobre micropython? 
# unete a nuestra comunidad https://www.facebook.com/ARDUINODAY19SC/
# EL DOMINIO DE  ESTE CODIGO ES PUBLICO
import machine, time

def toggle(p):
    p.value(not p.value())

pin = machine.Pin(4, machine.Pin.OUT)
while True:
    toggle(pin)
    time.sleep_ms(500)
    
