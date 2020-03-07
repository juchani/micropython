from machine import ADC
import time,machine
p12 =machine.Pin(12)
pwm=machine.PWM(p12)
adc=ADC(0)
while 1:
	print(adc.read())
	pwm.duty(adc.read())
	time.sleep_ms(500)
