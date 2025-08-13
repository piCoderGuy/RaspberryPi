import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
LED5 = 37
LED4 = 35
LED3 = 33
LED2 = 31
LED1 = 29

GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)
GPIO.setup(LED4,GPIO.OUT)
GPIO.setup(LED5,GPIO.OUT)
count =0
counted = 0
answer = 0
resulted = ''
    
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
while cycles > 0:
    time.sleep(.5)
    result = ''
    resulted = ''
    if count == 0:
        result = '00000'
    while count > 0:
        result = str(count%2) + result
        count = count //2
    resulted = resulted + str(result)
    if len (resulted) < 1:
        resulted = "00000" + result
    if len (resulted) < 2:
        resulted = "0000" + result
    if len (resulted) < 3:
        resulted = "000" + result
    if len (resulted) < 4:
        resulted = "00" + result
    if len (resulted) < 5:
        resulted = "0" + result
    
    
    print (resulted)
    if (resulted[4]) =='1':
        GPIO.output(LED1,1)
    else:
        GPIO.output(LED1,0)
    if (resulted[3]) =='1':
        GPIO.output(LED2,1)
    else:
        GPIO.output(LED2,0)
    if (resulted[2]) =='1':
        GPIO.output(LED3,1)
    else:
        GPIO.output(LED3,0)
    if (resulted[1]) =='1':
        GPIO.output(LED4,1)
    else:
        GPIO.output(LED4,0)
    if (resulted[0]) =='1':
        GPIO.output(LED5,1)
    else:
        GPIO.output(LED5,0)
    counted +=1
    if counted == 32:
        counted = 0
        
        if cycles > 1:
            print (f'{cycles-1} cycle(s) to go.')
        cycles -= 1
    count = counted
print ('All done.')  
time.sleep(2)       
GPIO.cleanup()
