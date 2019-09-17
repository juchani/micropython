# ejemplo micropython 
# te interesa mas sobre micropython? 
# unete a nuestra comunidad https://www.facebook.com/ARDUINODAY19SC/
# EL DOMINIO DE  ESTE CODIGO ES PUBLICO
import machine                                                                                                                                    
servo=machine.PWM(machine.Pin(12),freq=50)                                                                                                        
servo.duty(10)      