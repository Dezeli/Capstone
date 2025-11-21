from pymavlink import mavutil

conneection = mavutil.mavlink_connection('/dev/ttyAMA0', baud=57600)

print("Pixhawk ing...")

connection.wait_heartbeat()
print("Pixhawk good")
print(f"system ID: {connection.target_system}, component ID: {connection.target_component}") 
