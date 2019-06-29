# -*- coding:UTF-8 -*-
from __future__ import division								
import time
 
# Import the PCA9685 module.
import Adafruit_PCA9685										

pwm = Adafruit_PCA9685.PCA9685()					

def set_servo_angle(channel, angle):					
	date=4096*((angle*11)+500)/20000
	pwm_value = int(date)			
	pwm.set_pwm(channel, 0, pwm_value)

# Set frequency to 50hz, good for servos.
pwm.set_pwm_freq(50)
 
print 'Moving servo on channel x, press Ctrl-C to quit...'

def forward():
	set_servo_angle(4, 160)
	time.sleep(0.5)
	set_servo_angle(4, 30)
	time.sleep(0.5)


def turn_right():
	set_servo_angle(4, 30)
	time.sleep(0.5)
	set_servo_angle(4, 95)
	time.sleep(0.5)


def turn_left():
	set_servo_angle(4, 160)
	time.sleep(0.5)
	set_servo_angle(4, 95)
	time.sleep(0.5)

set_servo_angle(4, 95)
