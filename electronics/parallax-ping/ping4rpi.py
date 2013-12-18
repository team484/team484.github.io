#!/usr/bin/python
# adapted from code at http://www.raspberrypi.org/phpBB3/viewtopic.php?t=36593&p=317684
#
# Measure distance using an ultrasonic module in a loop.
#
import time
import RPi.GPIO as GPIO

#
# RPi pin used for measurement
#
GPIO_TRIGECHO = 23

def measure():
	# This function measures a distance
	# Pulse the trigger/echo line to initiate a measurement
	GPIO.output(GPIO_TRIGECHO, True)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGECHO, False)
	#ensure start time is set in case of very quick return
	start = time.time()

	# set line to input to check for start of echo response
	GPIO.setup(GPIO_TRIGECHO, GPIO.IN)
	while GPIO.input(GPIO_TRIGECHO)==0:
		start = time.time()

	# Wait for end of echo response
	while GPIO.input(GPIO_TRIGECHO)==1:
		stop = time.time()

	GPIO.setup(GPIO_TRIGECHO, GPIO.OUT)
	GPIO.output(GPIO_TRIGECHO, False)

	elapsed = stop-start
	distance = (elapsed * 34300)/2.0

	return distance

def measure_average():
	# This function takes 3 measurements and
	# returns the average.
	distance1=measure()
	time.sleep(0.1)
	distance2=measure()
	time.sleep(0.1)
	distance3=measure()
	distance = distance1 + distance2 + distance3
	distance = distance / 3
	print "raw %.1f" % distance1," %.1f" % distance2," %.1f" % distance3,
	return distance

# -----------------------
# Main Script
# -----------------------

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi

print "Ultrasonic Measurement"

# Set pins as output and input
GPIO.setup(GPIO_TRIGECHO,GPIO.OUT)  # Initial state as output

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGECHO, False)

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:
	while True:
		distance = measure_average()
		print "  Average: %.1f cm" % distance
		time.sleep(1)
except KeyboardInterrupt:
	# User pressed CTRL-C
	# Reset GPIO settings
	GPIO.cleanup()
