import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin number for the button
BUTTON_PIN = 13

# Set up the GPIO pin for reading
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # Read the state of the button
        button_state = GPIO.input(BUTTON_PIN)
        
        if button_state == GPIO.LOW:
            print("Button pressed")
        
        # Wait for a short time before reading again
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nExiting...")
finally:
    # Clean up GPIO settings
    GPIO.cleanup()
