#!/usr/bin/python3
#
# flash the output LEDs one by one
#

from time import sleep
import pifacedigitalio as pfio

MAX_BUTTON = 4

pfio.init()
try:
	current_state = []
	for button in range(0, MAX_BUTTON):
		current_state.append(pfio.digital_read(button))

	while (True):
		for button in range(0,MAX_BUTTON):
			value = pfio.digital_read(button)
			if value != current_state[button]:
				print("Button %d: %d" % (button, value))
				current_state[button] = value

except KeyboardInterrupt:
	print("bye!")

pfio.deinit()
