from gpiozero import LED
from time import sleep

red = LED(18)
yellow = LED(24)
green = LED(23)

while True:
    red.on()
    yellow.off()
    green.off()
    sleep(15)
    
    yellow.on()
    
    green.off()
    sleep(2)
    
    green.on()
    yellow.off()
    red.off()
    sleep(10)
    