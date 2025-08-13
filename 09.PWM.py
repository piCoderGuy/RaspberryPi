# PWM MODULATION ON PI
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
LEDpin = 37
downPin = 40
GPIO.setup(downPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
upPin = 40
GPIO.setup(upPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LEDpin,GPIO.OUT)
GPIO.output(LEDpin,1)

sleep(3)
GPIO.output(LEDpin,0)
myPWM=GPIO.PWM(LEDpin,100)	# 100 is frequency
myPWM.start(10)				# 10 is % of time on
sleep(3)
myPWM.ChangeDutyCycle(75)
sleep(3)
myPWM.ChangeFrequency(200)
myPWM.ChangeDutyCycle(50)

sleep(3)
myPWM.stop()
GPIO.cleanup()
