#!usr/bin/env python

import time
import pigpio

OPEN_PW = 1480
CLOSE_PW = 2200
SERVO=10

pi = pigpio.pi()

pi.set_servo_pulsewidth(SERVO, CLOSE_PW)

while True:
    time.sleep(1)
    pi.set_servo_pulsewidth(SERVO, OPEN_PW)
    time.sleep(1)
    pi.set_servo_pulsewidth(SERVO, CLOSE_PW)
