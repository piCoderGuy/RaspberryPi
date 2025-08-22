# Add a potentiometer and 3 colored LED's to a board.
# connected the potentiometer to a ADC pin (I used 28)
# As you turn the POT the LED's will change from Green to Blue to slow flashing red and fast flashing red
# The flashing is controlled by measuring time rather than time.sleep'ing the program
# This means there is no interuption to your program which could be doing other things.

from machine import Pin
import time
potPin = 28
greenAlert = 7
redAlert = 6
blueAlert = 8
greenLEDpot = Pin(greenAlert, Pin.OUT)
redLEDpot = Pin(redAlert, Pin.OUT)
blueLEDpot = Pin(blueAlert, Pin.OUT)
greenLEDpot.value(0)
redLEDpot.value(0)
blueLEDpot.value(0)
potVal = 0
myPot = machine.ADC(potPin) 	# ADC = Analog Digital Converter
actionTime = time.ticks_ms() + 250
criticalTime = time.ticks_ms() + 125
while True:
    newTimer = time.ticks_ms()
    potVal=myPot.read_u16()
    myVal=(100/(65535-336))*potVal
    print(myVal)
    time.sleep(.1)
    if myVal<33:
        greenLEDpot.value(0)
        blueLEDpot.value(1)
        redLEDpot(0)
    
    if myVal >=33 and myVal <66:
        greenLEDpot.value(1)
        blueLEDpot.value(0)
        redLEDpot(0)
    
    if myVal>=66 and myVal<=90:
        if newTimer < actionTime:
            greenLEDpot.value(0)
            blueLEDpot.value(0)
            redLEDpot(1)
    
    if myVal>=66 and myVal<=90:
        if newTimer > actionTime:
            greenLEDpot.value(0)
            blueLEDpot.value(0)
            redLEDpot(0)
    
    if myVal>90:
        if newTimer < criticalTime:
            greenLEDpot.value(0)
            blueLEDpot.value(0)
            redLEDpot(1)
    
    if myVal>90:
        if newTimer > criticalTime:
            greenLEDpot.value(0)
            blueLEDpot.value(0)
            redLEDpot(0)
            
    if newTimer > actionTime+500:
        actionTime = time.ticks_ms() + 250
    if newTimer > criticalTime+125:
        criticalTime = time.ticks_ms() + 125
