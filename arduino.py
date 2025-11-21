import serial
import time
from pymavlink import mavutil

arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
time.sleep(2)
print("Arduino connected")

pixhawk = mavutil.mavlink_connection('/dev/ttyAMA0', baud=57600)
pixhawk.wait_heartbeat()
print("Pixhawk connected")

def send_to_arduino(cmd):
    arduino.write(cmd.encode())
    print(f"Send a command: {cmd}")

def stop():
    send_to_arduino('S')

def forward():
    send_to_arduino('F')

def backward():
    send_to_arduino('B')

def left():
    send_to_arduino('R')

try:
    print("Autonomous Car test starts")
    forward()
    time.sleep(2)
    right()
    time.sleep(1)
    backward()
    time.sleep(2)
    left()
    time.sleep(1)
    stop()
    ptint("test finish")

except KeyboardInterrupt:
    print("emergency stop...")
    stop()

except Exception as e:
    print(f"Error: {e}")
    stop()
