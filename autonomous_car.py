import serial
import time
import RPi.GPIO as GPIO

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)

TRIG = 23
ECHO = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(ECHO) == 0:
        start_time = time.time()
    while GPIO.imput(ECHO) == 1:
        stop_time = time.time()

    distance = (stop_time - start_time) * 34300 / 2
    return distance

def send_command(cmd):
    arduino.write(cmd.encode())
    print(f"{Raspberry pie -> Arduino} {cmd}")

def autonomous_drive():
    try:
        while True:
            dist = get_distance()
            print(f"Distance: {dist:.2f}cm")

            if dist < 30:
                send_command('S')
                time.sleep(0.3)
                send_command('R')
                time.sleep(0.5)
                send_command('S')
            else:
                send_command('F')

            time.sleep(0.2)

     except KeyboardInterrupt:
         print("stopped")
         send_command('S')
         GPOI.cleanup()

if __name__ =="__main__":
    autonomous_drive()
