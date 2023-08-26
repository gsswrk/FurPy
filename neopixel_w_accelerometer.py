import time
import board
import busio
import adafruit_lis3dh
from digitalio import DigitalInOut
import neopixel
from rainbowio import colorwheel

# Initialize I2C bus and LIS3DH accelerometer
i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_lis3dh.LIS3DH_I2C(i2c)

# Initialize NeoPixels
pixel_pin1 = board.D18  # Replace "DX" with the BCM pin number connected to the DIN pin of NeoPixel 1
#pixel_pin2 = board.D2  # Replace "DY" with the BCM pin number connected to the DIN pin of NeoPixel 2
num_pixels = 2  # Change this to the number of NeoPixels you have per strip
pixels1 = neopixel.NeoPixel(pixel_pin1, num_pixels, auto_write=False)
#pixels2 = neopixel.NeoPixel(pixel_pin2, num_pixels, auto_write=False)

# Function to transmit accelerometer data to Raspberry Pi
def transmit_accel_data():
    # Read accelerometer data
    x, y, z = accelerometer.acceleration
    # Here you can send the data to the Raspberry Pi in any desired format
    # For example, you can use a serial connection or any other communication protocol
    # Optionally, you can update NeoPixel colors based on the accelerometer data
    # Example:
    #pixels1.fill(0, (int(abs(x) / 9.8 * 255)), 0)
    # pixels1.fill((int(abs(x) / 9.8 * cwheelnum), elnum)))
    # Red color based on x-axis acceleration
    #pixels1.fill((0, int(abs(y) / 9.8 * 255), 0))  # Green color based on y-axis acceleration
    pixels1.fill((0, int(abs(y) / 9.8 * 255), int(abs(x) / 9.8 * 255)))
    pixels1.show()
    # pixels2.show()

#if __name__ == "__main__":
#    try:
while True:
#        for cwheelnum in range(255):
    transmit_accel_data()
    time.sleep(0.1)  # Adjust the sleep time as needed
#   except KeyboardInterrupt:
        # Clean up any resources
#       pass
