import RPi.GPIO as GPIO
import time

# Motor Pins
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 2
ENA = 16
ENB = 13

# Sensor Pins
leftpin1 = 3
leftpin2 = 5
rightpin1 = 4
rightpin2 = 18

# Button
key = 8

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup motor pins
motor_pins = [IN1, IN2, IN3, IN4, ENA, ENB]
for pin in motor_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

# Setup sensor pins
sensor_pins = [leftpin1, leftpin2, rightpin1, rightpin2]
for pin in sensor_pins:
    GPIO.setup(pin, GPIO.IN)

# Setup button
GPIO.setup(key, GPIO.IN)

# Motor control functions
def forward():
    GPIO.output(IN1, 1)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 1)
    GPIO.output(IN4, 0)
    GPIO.output(ENA, 1)
    GPIO.output(ENB, 1)

def left():
    GPIO.output(IN1, 0)
    GPIO.output(IN2, 1)
    GPIO.output(IN3, 1)
    GPIO.output(IN4, 0)
    GPIO.output(ENA, 1)
    GPIO.output(ENB, 1)

def right():
    GPIO.output(IN1, 1)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 0)
    GPIO.output(IN4, 1)
    GPIO.output(ENA, 1)
    GPIO.output(ENB, 1)

def stop():
    GPIO.output(ENA, 0)
    GPIO.output(ENB, 0)

print("Waiting for button press to start...")
while GPIO.input(key) == 1:
    time.sleep(0.1)

print("Starting line following...")

try:
    while True:
        L1 = GPIO.input(leftpin1)
        L2 = GPIO.input(leftpin2)
        R1 = GPIO.input(rightpin1)
        R2 = GPIO.input(rightpin2)

        # Adjust this logic based on how your sensors detect black (usually black = LOW)
        if L1 == 0 and R2 == 0:
            forward()
        elif L1 == 0:
            left()
        elif R2 == 0:
            right()
        else:
            stop()

        time.sleep(0.01)

except KeyboardInterrupt:
    pass

stop()
GPIO.cleanup()
