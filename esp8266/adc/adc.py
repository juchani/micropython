from machine import ADC
import time
adc=ADC(0)
while 1:
	print(adc.read())
	time.sleep_ms(500)
