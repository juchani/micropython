import machine 
p12 =machine.Pin(12)
pwm=machine.PWM(p12)
pwm.duty(512)  #la mitad
