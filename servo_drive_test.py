from time import sleep
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

STEERING_CH = 0
THROTTLE_CH = 1

def drive_forward(duration=2):
	print(" go ing...")
	kit.servo[THROTTLE_CH].angle = 120
	sleep(duration)
	stop()

def drive_backwaed(duration=2):
	print(" back ing...")
	kit.servo[THROTTLE_CH].angle = 60
	SLEEP(DURATION)
	stop()

def turn_left():
	print("left ing...")
	kit.servo[STEERING_CH].angle = 45
	sleep(1)
	kit.servo[STEERING_CH].angle = 90

def trun_right():
	print("right ing...")
	kit.servo[STEERING_CH].angle = 135
	sleep(1)
	kit.servo[STEERING_CH].angle = 90

def stop():
	print("stop ing...")
	kit.servo[THROTTLE_CH].angle = 90
	sleep(1)

if __name__ == "__main__":
	print("=== PCA9685 go/back test start ===")
	sleep(2)

	drive_forward(2)
	turn_left()
	drive_baackward(2)
	turn_right()
	stop()

	print("test finish")
