# pelican_crossing.py
# A Python program to simulate the operation of a 
# pelican road crossing using Pimoroni's PiGlow.
#
# The PiGlow is a small add on board for the Raspberry Pi that
# provides 18 individually controllable LEDs
#
# For full details including setup, documentation and examples see:
# https://github.com/pimoroni/piglow#setting-up-your-raspberry-pi
# 
# Author: George W. Jopling
# https://github.com/georgejopling/piglow.git
#
# The code is commented for educational use.
#
# MIT License
# 
# Copyright (c) 2021 George W. Jopling.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#!/usr/bin/env python
# Import time - For pauses during traffic light sequence.
import time
# Import random - For simulating traffic volume during operation.
import random
# Import piglow - PiGlow Python library to control LED board.
import piglow
# Initialise LEDs.  PiGlow arms 1 & 3 = traffic, 2 = pedestrian.
# Clear all LEDs, illuminate green LED on arms 1 & 3,
# illuminate red LED on arm 2 and display the LED changes.
piglow.clear() 
piglow.single(1, 9, 255) 
piglow.single(3, 9, 255) 
piglow.single(2, 6, 255)
piglow.show()
# Start of loop to continuously repeat the code until stopped 
# at any time by pressing Ctrl+C on the keyboard.
try:
    while True: 
# Begin the operation of the crossing.
# Generate a random delay time to simulate a periodic press of the
# crossing button (10 to 20 seconds).
        random_delay = random.randint(10, 20)
        time.sleep(random_delay)
# Illuminate the white LED on arm 2 to simulate the Wait sign
# illumination.
        piglow.single(2, 5, 175)
        piglow.show()
# Generate a random delay time to simulate traffic volume delay
# in commencing operation (2 to 12 seconds).
        random_delay = random.randint(2, 12)
        time.sleep(random_delay)
# Extinguish green LED and illuminate amber LED on arms 1 & 3.
# Note - PiGlow orange LED is described as amber throughout.
        piglow.single(1, 9, 0)
        piglow.single(3, 9, 0)
        piglow.single(1, 7, 255)
        piglow.single(3, 7, 255)
        piglow.show()
# Pause on amber for 3 seconds.
        time.sleep(3.0)
# Extinguish amber LED and illuminate red LED on arms 1 & 3.
        piglow.single(1, 7, 0)
        piglow.single(3, 7, 0)
        piglow.single(1, 6, 255)
        piglow.single(3, 6, 255)
        piglow.show()
# Pause 1.5 seconds.
        time.sleep(1.5)           
# Extinguish red and white LED and illuminate green LED on arm 2.
        piglow.single(2, 6, 0)
        piglow.single(2, 5, 0)
        piglow.single(2, 9, 255)
        piglow.show()
# Pause 8 seconds.  Time for pedestrians to cross.
        time.sleep(8.0)
# Pulse (2 times) the green LED on arm 2 using a For loop.
        for i in range (2):
            piglow.single(2, 9, 0)
            piglow.show()
            time.sleep(0.200)
            piglow.single(2, 9, 255)
            piglow.show()
            time.sleep(0.800)
# After 2 pulses, extinguish red LED on arms 1 & 3.
            if i == 1:
                piglow.single(1, 6, 0)
                piglow.single(3, 6, 0)
                piglow.show()
# Pulse (10 times) the green LED on arm 2 and amber LED on arms 1 & 3
        for i in range (10):
            piglow.single(2, 9, 0)
            piglow.single(1, 7, 0)
            piglow.single(3, 7, 0)
            piglow.show()
            time.sleep(0.200)
            piglow.single(2, 9, 255)
            piglow.single(1, 7, 255)
            piglow.single(3, 7, 255)
            piglow.show()
            time.sleep(0.800)
# After 10 loops, extinguish green LED and illuminate
# red LED on arm 2.
            if i == 9:
                piglow.single(2, 9, 0)
                piglow.single(2, 6, 255)
                piglow.show()   
# Pulse (2 times) amber LED on arms 1 & 3.        
        for i in range (2):
            piglow.single(1, 7, 0)
            piglow.single(3, 7, 0)
            piglow.show()
            time.sleep(0.200)
            piglow.single(1, 7, 255)
            piglow.single(3, 7, 255)
            piglow.show()
            time.sleep(0.800)
# After 2 loops, extinguish amber LED and illuminate red LED on arms 1 & 3.
            if i == 1:
                piglow.single(1, 7, 0)
                piglow.single(3, 7, 0)
                piglow.single(1, 9, 255)
                piglow.single(3, 9, 255)
                piglow.show()
# Catch Ctr+C press on keyboard.
except KeyboardInterrupt: 
# Extinguish all LEDs on PiGlow and exit.
        piglow.clear()
        piglow.show()
