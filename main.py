from read_data import *
from servo import *
set_servo_angle(15, 95)
while 1:
	try:
		if read_data2() and read_data3():
			forward()
			
		if read_data2() and read_data3()==0:
			turn_right_low()
			
		if read_data3() and read_data2()==0:
			turn_left_low()
			
		if read_data1() and read_data2()==read_data3()==0:
			turn_right()
			
		if read_data4() and read_data2()==read_data3()==0:
			turn_left()
			
	except KeyboardInterrupt:
		set_servo_angle(15, 95)
		break
