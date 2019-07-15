from gpiozero import LED
from time import sleep 

led = LED(18)
#led1 = LED(18)
while True:
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.2)
#    led1.on()
#    sleep(0.3)
#    led1.off()
#    sleep(0.3)
