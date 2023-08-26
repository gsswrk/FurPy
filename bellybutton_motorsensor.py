import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pin numbers
BUTTON_FORWARD_PIN = 17
BUTTON_END_PIN = 22
AIN1 = 23
AIN2 = 24
PWMA = 5
STBY = 25

# Set up GPIO pins
GPIO.setup(BUTTON_FORWARD_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_END_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(STBY, GPIO.OUT)

# Create PWM instance
pwm = GPIO.PWM(PWMA, 1000)  # Frequency = 1000 Hz

# Initialize motor control pins
GPIO.output(STBY, GPIO.HIGH)  # Enable motor driver

try:
    while True:
        forward_button_state = GPIO.input(BUTTON_FORWARD_PIN)
        end_button_state = GPIO.input(BUTTON_END_PIN)

        if forward_button_state == GPIO.LOW:
            print("Moving forward")
            GPIO.output(AIN1, GPIO.HIGH)
            GPIO.output(AIN2, GPIO.LOW)
            # GPIO.output(PWMA, GPIO.HIGH)  # Start motor
            pwm.start(100)

            while end_button_state == GPIO.HIGH:
                end_button_state = GPIO.input(BUTTON_END_PIN)
            
            pwm.stop()
            time.sleep(.5)
            print("Moving in reverse")
            GPIO.output(AIN1, GPIO.LOW)
            GPIO.output(AIN2, GPIO.HIGH)
            pwm.start(100)
            time.sleep(0.5)
            pwm.stop()
        
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nExiting...")
finally:
    # Clean up GPIO settings
    GPIO.cleanup()
