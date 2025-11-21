from pymavlink import mavuyil
import time
import singal
import sys

PORT = '/dev/ttyAMA0'
BAUD = 57600
SPEED = 0.5

print("Pixhawk connecting...")
master = mavutil.mavlink_connection(PORT, baud=BAUD)
master.wait_heartbeat()
print(f"connected (System ID: {master.target_system})")

master.set_mode_apm('GUIDED')
print("Moter ARM finish")
time.sleep(2)

def send_velocity(vx, vy, vz=0):
    master.mav.set_position_target_local_ned_send(
    0,
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_FRAME_LOCAL_NED,
    0b0000111111000111,
    0, 0, 0,
    vx, vy, vz,
    0, 0, 0,
    0, 0
)

def forward(speed=SPEED):
    print("go")
    send_velocity(speed, 0)

def backward(speed=SPEED):
    print("back")
    send_velocity(-speed, 0)

def left(speed=SPEED):
    print("left")
    send_velocity(0, -speed)

def right(speed=SPEED):
    print("right")
    send_velocity(0, speed)

def stop():
    print("stop")
    send_velocity(0, 0)

def shutdown(sig=None, frame=None):
    print("|n E,ergency shutdown and termination...")
    stop()
    time.sleep(1)
    master.arducopter_disarm()
    print("Mode DISARM finish")
    sys.exit(0)

signal.signal(signal.SIGINT, shutdown)
signal.signal(signal.SIGTERM, shutdown)

try:
    print("Start autonomous vehicle driving")

    forward(0.6)
    time.sleep(2)

    right(0.5)
    time.sleep(1)

    forward(0.6)
    time.sleep(2)

    left(0.5)
    time.sleep(2)

    stop()
    time.sleep(1)

    shutdown()

except Exception as e:
    print(f"Error: {e}")
    shutdown()
