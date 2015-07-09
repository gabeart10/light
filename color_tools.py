import RPi.GPIO as GPIO
#Thes are my GPIO tools!


def all_off(p):
    for pin in p:
        GPIO.output(pin, 0)

def all_out(op):
    GPIO.setmode(GPIO.BCM)
    for pin in op:
        GPIO.setup(pin, GPIO.OUT)

def red_on(r,g,b):
    GPIO.output(r, 1)

def green_on(r,g,b):
    GPIO.output(g, 1)

def blue_on(r,g,b):
    GPIO.output(b, 1)

def cyan_on(r,g,b):
    GPIO.output(b, 1)
    GPIO.output(g, 1)

def magenta_on(r,g,b):
    GPIO.output(r, 1)
    GPIO.output(b, 1)

def yellow_on(r,g,b):
    GPIO.output(r, 1)
    GPIO.output(g, 1)

def white_on(r,g,b):
    GPIO.output(r, 1)
    GPIO.output(g, 1)
    GPIO.output(b, 1)
 
def white_off(r,g,b):
    GPIO.output(r, 0)
    GPIO.output(g, 0)
    GPIO.output(b, 0)

def red_off(r,g,b):
    GPIO.output(r, 0)

def green_off(r,g,b):
    GPIO.output(g, 0)

def blue_off(r,g,b):
    GPIO.output(b, 0)

def cyan_off(r,g,b):
    GPIO.output(g, 0)
    GPIO.output(b, 0)

def magenta_off(r,g,b):
    GPIO.output(r, 0)
    GPIO.output(b, 0)

def yellow_off(r,g,b):
    GPIO.output(r, 0)
    GPIO.output(g, 0)
