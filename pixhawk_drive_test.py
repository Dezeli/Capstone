from pymavlink import mavutil
from time import sleep

print("pixhack connect ing...")
connection.wait_heartbeat()
print("pixhawk connect finish")

def rc_override(throttle=1500, steering=1500):
	"""
	RC Override (Pixhawk RC pressure)
	channel 1: steering
	channel 3: throttle
	"""
	connection.mav.rc_channels_override_send(
		connection.target_system,
		connection.target_component,
		steering,
		0,
		throttle,
		0, 0, 0, 0, 0
	)
	print(f"RC Override -> throttle={throttle}, steering={steeering}")

def stop():
	rc_override(throttle=1500, steering=1500)
	print("stop signal")

def drive_forward(duration=2):
	print("go!")
	rc_override(throttle=1600, steering=1500)
	sleep(duration)
	stop()

def srive_backwaed(duration=2):
	print("back!")
	rc_override(throttle=1400, steering=1500)
	sleep(duration)
	stop()

def turn_left():
	print("left!")
	rc_override(throttle=1500, steering=1300)
	sleep(1)
	stop()

def turn_right():
	print("right!")
	rc_override(throttle=1500, steering=1700)
	sleep(1)
	stop()

if __name__ == "__main__":
	print("=== Pixhawk RC Override test start ===")
	sleep(2)

	drive_forward(2)
	turn_left()
	drive_backward(2)
	turn_right()
	stop()

	print("test finish") 

