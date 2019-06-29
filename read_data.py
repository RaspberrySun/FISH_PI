import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(0, GPIO.IN)
GPIO.setup(0, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(2, GPIO.IN)
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3, GPIO.IN)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN)
GPIO.setup(21,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN)
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)
def read_data1():
	if GPIO.input(7):
		return 0
	else:
		return 1
def read_data2():
	if GPIO.input(0):
		return 0
	else:
		return 1
def read_data3():
	if GPIO.input(2):
		return 0
	else:
		return 1
def read_data4():
	if GPIO.input(3):
		return 0
	else:
		return 1
def read_data5():
	if GPIO.input(21):
		return 0
	else:
		return 1
def read_data6():
	if GPIO.input(22):
		return 0
	else:
		return 1
while 1:
	read_data1()
