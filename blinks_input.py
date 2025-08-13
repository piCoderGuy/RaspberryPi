import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
redLED = 37
GPIO.setup(redLED,GPIO.OUT)	# setup pin 11 as an output
for i in range(3):
    GPIO.output(redLED,True)	# or (11,1)
    time.sleep(1)
    GPIO.output(redLED,False)	# or (11,0)
    time.sleep(1)
run = 1
invalid = True
while run == 1:
    question = input('Do you want the LED ON(o) or OFF(f) or flash 1-9 - Quit(q)? ')
    try:
        if (str(question) == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9'):
            blink = int(question)
            invalid = False
            for blinks in range (blink):
                GPIO.output(redLED,True)	# or (11,1)
                time.sleep(.5)
                print (blink - blinks)
                GPIO.output(redLED,False)	# or (11,0)
                time.sleep(.5)
        
    except Exception as e:
        pass
    if (str(question.lower())) == ('o'):
        GPIO.output(redLED,True)
        invalid = False
    if (str(question.lower())) == ('f'):
        GPIO.output(redLED,False)
        invalid = False
    if (str(question.lower())) == ('q'):
        run = 0
        invalid = False
    if invalid == True:
        print ('Invalid option!')
    invalid = True
GPIO.cleanup()
