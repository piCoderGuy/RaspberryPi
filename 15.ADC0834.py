import RPi.GPIO as GPIO
import ADC0834
from time import sleep

GPIO.setmode(GPIO.BCM)
ADC0834.setup()
try:
    while True:
        AnalogueValue = ADC0834.getResult(0)
        print (AnalogueValue)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO OK')
