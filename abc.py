from dronekit import connect

vehicle = connect('/dev/ttyAMA0', wait_ready=True, baud=57600)
print("Connection successful!")

vehicle.close()
