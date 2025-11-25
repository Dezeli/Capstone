from pymavlink import mavutil
import time

master = mavutil.mavlink_connection('/dev/ttyAMA10', baud = 57600)
print("Pixhawk connecting...")
master.wait_heartbeat()
print(f"Pixhawk success(System ID: {master.target_system})")

master.set_mode_apm('GUIDED')
print("Mode: GUIDED finish")

master.arducopter_arm()
print("Moter finish")

time.sleep(2)

print("go test start (1s)")
master.mav.set_position_target_local_ned_send(
    0,
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_FRAME_LOCAL_NED,
    0b0000111111000111,
    0, 0, 0,
    0.5, 0, 0,
    0, 0, 0,
    0, 0
)

time.sleep(1)

print("stop")
master.mav.set_position_target_local_ned_send(
    0,
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_FRAME_LOCAL_NED,
    0b0000111111000111,
    0, 0, 0,
    0, 0, 0,
    0, 0, 0,
    0, 0,
)

time.sleep(1)

master.arducopter_disarm()
print("test finish and moter clear (DISARM)")
