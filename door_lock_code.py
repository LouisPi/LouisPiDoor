#!/usr/bin/python3

from pad4pi import rpi_gpio
import time
import Adafruit_SSD1306
import sys
from PIL import Image, ImageDraw, ImageFont
from gpiozero import Servo

myCorrection = 0.45
maxPW = (2.0+myCorrection)/1000
minPW = (1.0-myCorrection)/1000
servo = Servo(24, min_pulse_width = minPW, max_pulse_width = maxPW)
servo.mid()
time.sleep(1)
servo.detach()

RST = 24
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
#image = Image.new('1', (width, height))
#draw = ImageDraw.Draw(image)
#draw.rectangle((0,0,width,height), outline=0, fill=0)
#padding = -2
#top = padding
#bottom = height-padding
#x = 0
#font = ImageFont.truetype("roboto.ttf", 20)

entered_passcode = ""
correct_passcode = "8790"

def print_oled(text):
    disp.clear()
    disp.display()
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    padding = -2
    top = padding
    bottom = height-padding
    x = 0
    font = ImageFont.truetype("roboto.ttf", 20)
    draw.text((x, top), text, font=font, fill=255)
    disp.image(image)
    disp.display()

def cleanup():
    time.sleep(3)
    global keypad
    keypad.cleanup()
    disp.clear()
    disp.display()
    sys.exit()

def correct_passcode_entered():
    #print("Passcode accepted. Access granted.")
    print_oled("Access granted")
    servo.max()
    cleanup()

def incorrect_passcode_entered():
    #print("Incorrect passcode. Access denied.")
    print_oled("Access denied")
    cleanup()

def digit_entered(key):
    global entered_passcode, correct_passcode

    entered_passcode += str(key)
    #print(entered_passcode)
    print_oled(entered_passcode)

    if len(entered_passcode) == len(correct_passcode):
        if entered_passcode == correct_passcode:
            correct_passcode_entered()
        else:
            incorrect_passcode_entered()

def non_digit_entered(key):
    global entered_passcode

    if key == "*" and len(entered_passcode) > 0:
        entered_passcode = entered_passcode[:-1]
        print_oled(entered_passcode)

def key_pressed(key):
    try:
        int_key = int(key)
        if int_key >= 0 and int_key <= 9:
            digit_entered(key)
    except ValueError:
        non_digit_entered(key)

try:
    factory = rpi_gpio.KeypadFactory()
    keypad = factory.create_4_by_4_keypad() # makes assumptions about keypad layout and GPIO pin numbers

    keypad.registerKeyPressHandler(key_pressed)

    #print("Enter your passcode.")
    print_oled("Enter passcode")
    print("Press * to clear previous digit.")

    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print_oled("Goodbye")
finally:
    cleanup()
