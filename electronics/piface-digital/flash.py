#!/usr/bin/python3
#
# flash the output LEDs one by one
#

from time import sleep
import pifacedigitalio as pfio

pfio.init()
try:
	while (True):
		for loop in range(0,7):
			print("flashing %d" % loop)
			pfio.digital_write(loop,1)
			sleep(1)
			pfio.digital_write(loop,0)
			sleep(1)

except KeyboardInterrupt:
	print("Cleaning up")
	for loop in range(0, 7):
		pfio.digital_write(loop, 0)

pfio.deinit()
