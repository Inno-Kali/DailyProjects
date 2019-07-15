from gpiozero import LED
from time import sleep

red = LED(18)
blue = LED(23)

while True:
    red.on()
    blue.off()
    sleep(0.155)
    
    blue.on()
    red.off()
    sleep(0.3)