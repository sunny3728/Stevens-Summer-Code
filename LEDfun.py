#simple led functions for raspberry pi.
#written at summer workshop july 2015
import RPi.GPIO as GPIO
import time
repeat = 50
ypin2 = 22
ypin1 = 16
rpin2= 12
rpin1= 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ypin1,GPIO.OUT)
GPIO.setup(ypin2,GPIO.OUT)
GPIO.setup(rpin1,GPIO.OUT)
GPIO.setup(rpin2,GPIO.OUT)

def flash(unit):
    GPIO.output(ypin1,GPIO.LOW)
    time.sleep(unit)
    GPIO.output(rpin1,GPIO.LOW)
    time.sleep(unit)
    GPIO.output(ypin2,GPIO.LOW)
    time.sleep(unit)
    GPIO.output(rpin2,GPIO.LOW)
    time.sleep(unit)
    GPIO.output(rpin2,GPIO.HIGH)
    GPIO.output(ypin2,GPIO.HIGH)
    GPIO.output(rpin1,GPIO.HIGH)
    GPIO.output(ypin1,GPIO.HIGH)
    time.sleep(unit*2.0)
    return

for i in range(50):
    flash(.5)

GPIO.cleanup()
