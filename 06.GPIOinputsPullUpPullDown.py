import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
redLED = 16
readPin = 11
GPIO.setup(readPin,GPIO.IN)
GPIO.setup(redLED,GPIO.OUT)
GPIO.output(redLED,0)
try:
    while True:
        readVal=GPIO.input(readPin)
        print (readVal)
        if readVal == 0:
            GPIO.output(redLED,1)
        else:
            GPIO.output(redLED,0)
        time.sleep(.1)
except KeyboardInterrupt:
    GPIO.cleanup()
# readVal will return 1 for 3.3 volts down to 0 for zero volts
