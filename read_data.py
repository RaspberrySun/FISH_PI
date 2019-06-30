import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
PinList = [7, 11, 13, 15, 29, 31]
GPIO.setup(PinList, GPIO.IN)
GPIO.setup(PinList, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def read_data1():
	if GPIO.input(7):
		return 0
	else:
		return 1
def read_data2():
	if GPIO.input(11):
		return 0
	else:
		return 1
def read_data3():
	if GPIO.input(13):
		return 0
	else:
		return 1
def read_data4():
	if GPIO.input(15):
		return 0
	else:
		return 1
def read_data5():
	if GPIO.input(29):
		return 0
	else:
		return 1
def read_data6():
	if GPIO.input(31):
		return 0
	else:
		return 1

if __name__ == "__main__":
	print [read_data1(), read_data2(), read_data3(), read_data4(), read_data5(), read_data6()]
