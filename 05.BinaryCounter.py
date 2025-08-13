import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
LED1 = 37
LED2 = 35
LED3 = 33
LED4 = 31
LED5 = 29

GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)
GPIO.setup(LED4,GPIO.OUT)
GPIO.setup(LED5,GPIO.OUT)
count = 0
answer = 0
while answer == 0:
    
    
    try:
        cycles = int(input('How many cycles (1-9)? '))
        if cycles < 10:
            answer = 1
    
        if cycles >9:
            print ('Sorry invalid!')
        
    except Exception as e:
        print ('Invalid!')
        pass
        
while count < 32*cycles:
    time.sleep(.5)
    
    if (count %2)>0:
        GPIO.output(LED5,1)
    else:
        GPIO.output(LED5,0)
    if (count %4)>1:
        GPIO.output(LED4,1)
    else:
        GPIO.output(LED4,0)
    if (count %8)>3:
        GPIO.output(LED3,1)
    else:
        GPIO.output(LED3,0)
    if (count %16)>7:
        GPIO.output(LED2,1)
    else:
        GPIO.output(LED2,0)
    if (count %32)>15:
        GPIO.output(LED1,1)
    else:
        GPIO.output(LED1,0)
    print(GPIO.input(LED1),GPIO.input(LED2),GPIO.input(LED3),GPIO.input(LED4),GPIO.input(LED5))
    count = count + 1
    time.sleep(.5)
    
GPIO.cleanup()
