# Louis Pi Door Opening Code

The code uses a keypad to allow the user to enter a code. If the code matches the one preset access is granted by turning a small SG90 servo from the middle (locking a model door)to the max (allowing a model door to open). All text is shown on a 128 x 64 SSD1306 i2c OLED. Big thanks to Brett McLean (the creator of the pad4pi python library) for all the keypad code (https://github.com/brettmclean/pad4pi/blob/develop/rpi_gpio_demo2.py) and to Tony DiCola (Adafruit Industried) for the OLED code (https://github.com/adafruit/Adafruit_Python_SSD1306). 

Pin connections (BOARD) as follows:

OLED:
GND (Ground) --- Pin 6, 9, 14, 20, 25, 30, 34 or 39 (GND)
VDD (Power) --- Pin 1 or 17 (3.3V)
SCK (SCL) --- Pin 5
SDA --- Pin 3

Keypad:

See this diagram - http://www.theorycircuit.com/wp-content/uploads/2015/12/4x4-keypad-matrix.jpg

Rows 1 to 4 - 7, 8, 10 and 11
Columns 1 to 4 - 12, 13, 15 and 16

Servo:

If you are using a SG90 servo see this pinout - https://c1.staticflickr.com/8/7455/27397776234_48c85e9f22.jpg

Power - 2 or 4 (5V)
Ground - Pin 6, 9, 14, 20, 25, 30, 34 or 39 (GND)
Signal - 18
