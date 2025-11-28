import pigpio
import time
from pymavlink import mavutil

'''
sudo apt update
sudo apt install pigpio python3-pigpio
sudo systemctl enable pigpiod
sudo systemctl start pigpiod
'''

master = mavutil.mavlink_connection('/dev/ttyAMA0', baud=57600)
master.wait_heartbeat()
print("Pixhawk Connected")

def set_throttle(pwm):
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
        0,
        1,       # MAIN OUT 1 (스로틀)
        pwm,     # PWM 값
        0,0,0,0,0
    )

SERVO_PIN = 23

pi = pigpio.pi()
if not pi.connected:
    print("pigpio connection failed")
    exit(0)

CENTER = 1500
LEFT   = 1000
RIGHT  = 2000

def servo_center():
    pi.set_servo_pulsewidth(SERVO_PIN, CENTER)

def servo_left():
    pi.set_servo_pulsewidth(SERVO_PIN, LEFT)

def servo_right():
    pi.set_servo_pulsewidth(SERVO_PIN, RIGHT)

try:
    print("=== TEST START ===")

    # 1) 전진 2초
    print("전진 2초")
    servo_center()
    set_throttle(1600)
    time.sleep(2)

    # 정지 1초
    print("정지 1초")
    set_throttle(1500)
    time.sleep(1)

    # 2) 왼쪽 조향 2초
    print("왼쪽 2초")
    servo_left()
    time.sleep(2)

    # 정지(중앙) 1초
    print("정지 1초")
    servo_center()
    time.sleep(1)

    # 3) 오른쪽 조향 2초
    print("오른쪽 2초")
    servo_right()
    time.sleep(2)

    # 정지 1초
    print("정지 1초")
    servo_center()
    time.sleep(1)

finally:
    set_throttle(1500)
    pi.set_servo_pulsewidth(SERVO_PIN, 0)
    pi.stop()

    print("=== TEST END ===")
