import RPi.GPIO as GPIO

def all_off(p):
    for pin in p:
        GPIO.output(pin, 0)

def all_out(op):
    GPIO.setmode(GPIO.BCM)
    for pin in op:
        GPIO.setup(pin, GPIO.OUT)
