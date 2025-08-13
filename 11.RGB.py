from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
rLED = 36
gLED = 38
bLED = 40

rBTN = 33
gBTN = 35
bBTN = 37
GPIO.setup(rBTN,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(gBTN,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(bBTN,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(rLED,GPIO.OUT)
GPIO.setup(gLED,GPIO.OUT)
GPIO.setup(bLED,GPIO.OUT)
GPIO.output(rLED,0)
GPIO.output(gLED,0)
GPIO.output(bLED,0)
sleep(.1)

rBTNstate = 0
rBTNold = 1
gBTNstate = 0
gBTNold = 1
bBTNstate = 0
bBTNold = 1
redState = 0
grnState = 0
bluState = 0
try:
    while True:
        redBTN = GPIO.input(rBTN)
        grnBTN = GPIO.input(gBTN)
        bluBTN = GPIO.input(bBTN)
        #print (redBTN)
        if redBTN == 0 and rBTNold == 0:
            redState = not redState
            GPIO.output(rLED,redState)
            if redState == True:
                redOnOff = "on"
            else:
                redOnOff = "off"
            print (f'The red LED is {redOnOff}')
        if grnBTN == 0 and gBTNold == 0:
            grnState = not grnState
            GPIO.output(gLED,grnState)
            if grnState == True:
                grnOnOff = "on"
            else:
                grnOnOff = "off"
            print (f'The green LED is {grnOnOff}')
        if bluBTN == 0 and bBTNold == 0:
            bluState = not bluState
            GPIO.output(bLED,bluState)
            if bluState == True:
                bluOnOff = "on"
            else:
                bluOnOff = "off"
            print (f'The blue LED is {bluOnOff}')
        rBTNold = rBTNstate
        gBTNold = gBTNstate
        bBTNold = bBTNstate
        sleep(.3)
except KeyboardInterrupt:
    GPIO.cleanup()
    
GPIO.cleanup()
