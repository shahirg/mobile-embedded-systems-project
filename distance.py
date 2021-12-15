import RPi.GPIO as GPIO
import time

def get_distance():
    distance = 130
    while distance > 120 or distance < 70:

        try:
            GPIO.setmode(GPIO.BCM)
            TRIG = 23
            ECHO = 24

            GPIO.setup(TRIG, GPIO.OUT)
            GPIO.setup(ECHO, GPIO.IN)

            GPIO.output(TRIG, GPIO.LOW)
            time.sleep(2)
            GPIO.output(TRIG, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(TRIG, GPIO.LOW)

            while GPIO.input(ECHO) == 0:
                pulse_start = time.time()

            while GPIO.input(ECHO) == 1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration*17150
            distance = round(distance,2)

            print("distance", distance)

        finally:
            GPIO.cleanup()

    return

check_dist()