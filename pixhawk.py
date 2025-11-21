from pymavlink import mavutil

def get_pixhawk_data():
    connection = mavutil.mavlink_connection('/dev/ttyAMA0', baud=57600)
    connection.wait_heartbeat()
    print("Pixhawk connected")

    while True:
        msg = connection.recv_match(blocking=True)
        if not msg:
            continue
        if msg.get_type() == 'GLOBAL_POSITION_INT':
            lat = msg.lat / 1e7
            lon = msg.lon / 1e7
            alt = msg.alt / 1000
            print(f"GPS: {lat}, {lon}, {alt}m")
