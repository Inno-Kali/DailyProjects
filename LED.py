from gpiozero import LED
from time import sleep 

led = LED(18)

while True:
    led.on()
    sleep(4)
    led.off()
    sleep(1)
     led.on()
    sleep(4)
    led.off()
    sleep(1)-+
