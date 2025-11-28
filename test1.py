from pymavlink import mavutil
import time

master = mavutil.mavlink_connection('/dev/ttyAMA0', baud=57600)

master.wait_heartbeat()
print("Connected to Pixhawk")


def set_pwm(channel, pwm):
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
        0,
        channel,
        pwm,       # PWM 값 1600:전진, 1500:정지, 1400:후진
        0,0,0,0,0
    )

for i in range(3):
    print(f"=== {i+1}번째 루프 시작 ===")

    print("전진 3초")
    set_pwm(1, 1600)
    time.sleep(3)

    print("정지 2초")
    set_pwm(1, 1500)
    time.sleep(2)

    print("후진 3초")
    set_pwm(1, 1400)
    time.sleep(3)

    print("정지")
    set_pwm(1, 1500)
    time.sleep(2)

print("=== 테스트 완료 ===")
set_pwm(1, 1500)
