import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for motor control
PWMA = 5
AIN1 = 23
AIN2 = 24
STBY = 25

# Set up the GPIO pins
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(STBY, GPIO.OUT)

# Initialize motor control pins
GPIO.output(STBY, GPIO.HIGH)  # Enable motor driver

try:
    while True:
        # Move the motor forward
        GPIO.output(AIN1, GPIO.HIGH)
        GPIO.output(AIN2, GPIO.LOW)
        GPIO.output(PWMA, GPIO.HIGH)  # Start motor

        print("Motor moving forward")
        time.sleep(2)  # Run for 2 seconds

        # Stop the motor
        GPIO.output(PWMA, GPIO.LOW)

        # Reverse the motor
        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
        GPIO.output(PWMA, GPIO.HIGH)  # Start motor

        print("Motor moving in reverse")
        time.sleep(2)  # Run for 2 seconds

        # Stop the motor
        GPIO.output(PWMA, GPIO.LOW)

except KeyboardInterrupt:
    print("\nExiting...")
finally:
    # Clean up GPIO settings
    GPIO.cleanup()
