# ejemplo micropython 
# te interesa mas sobre micropython? 
# unete a nuestra comunidad https://www.facebook.com/ARDUINODAY19SC/
# EL DOMINIO DE  ESTE CODIGO ES PUBLICO

from machine import ADC
import time
adc=ADC(0)
while 1:
	print(adc.read())
	time.sleep_ms(500)
