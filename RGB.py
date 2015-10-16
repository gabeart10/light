import RPi.GPIO as GPIO
import time

pins = [14,15,18]

GPIO.setmode(GPIO.BCM)
#Brown,Black,White,Gray
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
p1 = GPIO.PWM(14, 50)
p2 = GPIO.PWM(15, 50)
p3 = GPIO.PWM(18, 50)

p1.start(0)
p2.start(0)
p3.start(0)


try:
    while True:
        for dc1 in range(0, 100, 1):
            p1.ChangeDutyCycle(dc1)
            time.sleep(0.05)
        for dc2 in range(100, 0, -1):
            p1.ChangeDutyCycle(dc2)
            time.sleep(0.05)
        for dc3 in range(0, 100, 1):
            p2.ChangeDutyCycle(dc3)
            time.sleep(0.05)
        for dc4 in range(100, 0, -1):
            p2.ChangeDutyCycle(dc4)
            time.sleep(0.05)
        for dc5 in range(0, 100, 1):
            p3.ChangeDutyCycle(dc5)
            time.sleep(0.05)
        for dc6 in range(100, 0, -1): 
            p3.ChangeDutyCycle(dc6)
            time.sleep(0.05)
        for dc7 in range(0, 100, 1): 
            p1.ChangeDutyCycle(dc7)
            p2.ChangeDutyCycle(dc7)
            p3.ChangeDutyCycle(dc7)
            time.sleep(0.05)
        for dc8 in range(100, 0, -1):
            p1.ChangeDutyCycle(dc8)
            p2.ChangeDutyCycle(dc8)
            p3.ChangeDutyCycle(dc8)
            time.sleep(0.05)
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()
