# PWM MODULATION ON PI
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
LEDpin = 37
downPin = 40
GPIO.setup(downPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
upPin = 38
GPIO.setup(upPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LEDpin,GPIO.OUT)
GPIO.output(LEDpin,1)
buttonUpState = 0
oldBtnUpState = 1
buttonDownState = 0
oldBtnDownState = 1
brightness = 10
myPWM=GPIO.PWM(LEDpin,100)	# 100 is frequency
myPWM.start(brightness)
try:
    while True:
        readUp = GPIO.input(upPin)
        readDown = GPIO.input(downPin)
        if readUp==1 and oldBtnUpState ==0:
                brightness += 10
                if brightness >= 100:
                    brightness = 99
                    
        oldBtnUpState = readUp
        sleep(.1)
        if readDown==1 and oldBtnDownState ==0:
                brightness -= 10
                if brightness <= 0:
                    myPWM.stop()
                    GPIO.output(LEDpin,0)
                    brightness = 0
        sleep(.1)
        oldBtnDownState = readDown
        if brightness > 0:
            #myPWM=GPIO.PWM(LEDpin,100)	# 100 is frequency
            myPWM.start(brightness)
            myPWM.ChangeDutyCycle(brightness)
        print(brightness)

except KeyboardInterrupt:
    myPWM.stop()
    GPIO.cleanup()
GPIO.cleanup()


