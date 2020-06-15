
# MICROPYTHON
## Es una  forma sencilla de programar microcontroladores 
![ESP32-Pinout.png](attachment:ESP32-Pinout.png)


```micropython
%serialconnect
```

    [34mConnecting to --port=COM4 --baud=115200 [0m
    [34mReady.
    [0m


```micropython
%serialconnect to --port=COM10 --baud=115200
```

    [34mConnecting to --port=COM10 --baud=115200 [0m
    [34m
    Are you sure your ESP-device is plugged in?[0m


```micropython
import os

print(os.listdir())
```

    ['boot.py']



```micropython
print(7%(5//2))
```

    1



```micropython
print ("hola mundo")

```

    hola mundo



```micropython
import os 
```


```micropython
print(os.listdir())
```

    ['boot.py']



```micropython
from machine import Pin as p
led=p(2,p.OUT)

```


```micropython
help(machine)
```

    object <module 'umachine'> is of type module
      __name__ -- umachine
      mem8 -- <8-bit memory>
      mem16 -- <16-bit memory>
      mem32 -- <32-bit memory>
      freq -- <function>
      reset -- <function>
      reset_cause -- <function>
      unique_id -- <function>
      idle -- <function>
      sleep -- <function>
      deepsleep -- <function>
      disable_irq -- <function>
      enable_irq -- <function>
      time_pulse_us -- <function>
      RTC -- <class 'RTC'>
      Timer -- <class 'Timer'>
      WDT -- <class 'WDT'>
      Pin -- <class 'Pin'>
      Signal -- <class 'Signal'>
      PWM -- <class 'PWM'>
      ADC -- <class 'ADC'>
      UART -- <class 'UART'>
      I2C -- <class 'I2C'>
      SPI -- <class 'HSPI'>
      DEEPSLEEP -- 4
      PWRON_RESET -- 0
      HARD_RESET -- 6
      DEEPSLEEP_RESET -- 5
      WDT_RESET -- 1
      SOFT_RESET -- 4
    


```micropython
led.on()
```


```micropython
led.off()
```


```micropython
print(led.value())
```

    0



```micropython
variable1=1.5

```


```micropython
print(type(variable1))
```

    <class 'float'>
    


```micropython
from machine import ADC
import time
adc=ADC(0)
while 1:
	print(adc.read())
	time.sleep_ms(500)

```

    Traceback (most recent call last):
      File "<stdin>", line 3, in <module>
    ValueError: expecting a pin
    


```micropython
help(modules)
```

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'modules' is not defined
    


```micropython

```
