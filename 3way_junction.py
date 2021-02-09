# 
# 3way_junction.py
# A Python program to simulate a 3 way traffic light
# controlled road junction using Pimoroni's PiGlow.
# 
# The PiGlow is a small add on board for the Raspberry Pi that
# provides 18 individually controllable LEDs.
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
# Initialise LEDs.  PiGlow arms 1, 2 & 3 = junctions.
# Clear all LEDs and illuminate red LED on arms 1, 2 & 3)
# and display the changes.
piglow.clear()
piglow.single(1, 6, 255)
piglow.single(2, 6, 255)
piglow.single(3, 6, 255)
piglow.show()
# Start of loop to continuously repeat the code until stopped 
# at any time by pressing Ctrl+C on the keyboard.
try:
    while True:     
# Junction 1 (using arm 1 LEDs).
# Sequence:
# Pause on red LED for 2.5 seconds,
# Illuminate amber LED,
# Pause on red and amber LED for 2.5 seconds,
# Extinguish red and amber LED,
# Illuminate green LED.
# Note - PiGlow orange LED is described as amber throughout.
        time.sleep(2.5)
        piglow.single(1, 7, 255)
        piglow.show()
        time.sleep(2.5)
        piglow.single(1, 6, 0)
        piglow.single(1, 7, 0)
        piglow.single(1, 9, 255)
        piglow.show()
# Generate a random delay time to simulate traffic volume
# at the junction (10 to 20 seconds).
        random_delay = random.randint(10, 20)
        time.sleep(random_delay)
# Sequence:
# Extinguish green LED,
# Illuminate amber LED,
# Pause on amber LED for 3 seconds,
# Extinguish amber LED,
# Illuminate red LED.  
        piglow.single(1, 9, 0)
        piglow.single(1, 7, 255)
        piglow.show()
        time.sleep(3.0)
        piglow.single(1, 7, 0)
        piglow.single(1, 6, 255)
        piglow.show()
# Junction 2 (using arm 2 LEDs).  
# **Same sequence as shown for arm 1**.       
        time.sleep(2.5)
        piglow.single(2, 7, 255)
        piglow.show()
        time.sleep(2.5)
        piglow.single(2, 6, 0)
        piglow.single(2, 7, 0)
        piglow.single(2, 9, 255)
        piglow.show()
# Generate a random delay time to simulate traffic volume
# at the junction (10 to 20 seconds).
        random_delay = random.randint(10, 20)
        time.sleep(random_delay)
# **Same sequence as shown for arm 1**  
        piglow.single(2, 9, 0)
        piglow.single(2, 7, 255)
        piglow.show()
        time.sleep(3.0)
        piglow.single(2, 7, 0)
        piglow.single(2, 6, 255)
        piglow.show()
# Junction 3 (using arm 3 LEDs).  
# **Same sequence as shown for arm 1**
        time.sleep(2.5)
        piglow.single(3, 7, 255)
        piglow.show()
        time.sleep(2.5)
        piglow.single(3, 6, 0)
        piglow.single(3, 7, 0)
        piglow.single(3, 9, 255)
        piglow.show()
# Generate a random delay time to simulate traffic volume
# at the junction (10 to 20 seconds).
        random_delay = random.randint(10, 20)
        time.sleep(random_delay)
# **Same sequence as shown for arm 1**.      
        piglow.single(3, 9, 0)
        piglow.single(3, 7, 255)
        piglow.show()
        time.sleep(3.0)
        piglow.single(3, 7, 0)
        piglow.single(3, 6, 255)
        piglow.show()
# Catch Ctr+C press on keyboard
except KeyboardInterrupt: 
# Extinguish all LEDs on PiGlow and exit.
    piglow.clear()
    piglow.show()
