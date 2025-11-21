#drive_test.py
from time import sleep
from adafruit_servokit import ServoKit

#16channel PWM board
kit = ServoKit(channels=16) 

#channel
STEERING_CHANNEL = 0
THROTTLE_CHANNEL = 1

def drive_forwaed(duration=2):
	"""go"""
	print("go start!")
	kit.servo[THROTTLE_CHANNEL].angle = 120
	sleep(duration)
	stop()

def drive_backward(duration=2):
	"""back"""
	print("back start!")
	kit.servo[THROTTLE_CHANNEL].angle = 60
	sleep(duration)
	stop()

def stop():
	"""stop"""
	kit.servo[THROTTLE_CHANNEL].angle = 90
	print("stop (90 signal)")

if __name__ == "__main__":
	print("test start: ESC finish.")
	sleep(2)

	drive_forwaed(2)
	sleep(1)
	drive_backwaed(2)
	stop()
	print("test finish!")

