from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
redLED = 38
readPin = 40
GPIO.setup(readPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(redLED,GPIO.OUT)
GPIO.output(redLED,0)
ledState = 0
lastState = 1
try:
    while True:
        readVal=GPIO.input(readPin)
        print (readVal)
        if readVal==1 and lastState ==0:
            ledState = not ledState
            GPIO.output(redLED, ledState)
        lastState = readVal
        
        sleep(.1)
except KeyboardInterrupt:
    GPIO.cleanup()
