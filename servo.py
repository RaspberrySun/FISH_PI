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

def forward_fast():
	set_servo_angle(15, 160)
	time.sleep(0.3)
	set_servo_angle(15, 30)
	time.sleep(0.3)

def forward_middle():
	set_servo_angle(15, 50)
	time.sleep(0.25)
	set_servo_angle(15, 140)
	time.sleep(0.25)

def turn_right_low():
	set_servo_angle(15, 55)
	time.sleep(0.4)
	set_servo_angle(15, 95)
	time.sleep(0.4)

def turn_right():
	set_servo_angle(15, 30)
	time.sleep(0.4)
	set_servo_angle(15, 95)
	time.sleep(0.4)

def turn_left_low():
	set_servo_angle(15, 135)
	time.sleep(0.4)
	set_servo_angle(15, 95)
	time.sleep(0.4)

def turn_left():
	set_servo_angle(15, 160)
	time.sleep(0.4)
	set_servo_angle(15, 95)
	time.sleep(0.4)

if __name__ == "__main__":
	forward()
