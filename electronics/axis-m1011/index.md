---
layout: default
title: Axis M1011 Network Camera
categories: [ hardware, public]
tags: [ camera, networking, vision]
---

[User Manual](um_m10_46940_en_1203.pdf) - [source](http://www.axis.com/files/manuals/um_m10_46940_en_1203.pdf)

[Firmware downloads](http://www.axis.com/techsup/firmware.php) - current version as of Jan 19, 2014 is 5.20.2

Power
-----
Power requirements (from the back of the device): 5V at 1.5A

Defaults
--------
Network address: 192.168.0.80

User name: root

Password: (set when first accessed)

Reset
-----
To reset to factory settings:

1.Disconnect power from the camera.
2.Press and hold the Control button and reconnect power.
3.Keep the Control button pressed until the Status indicator flashes amber (this may take up to 15 seconds).
4.Release the Control button. When the Status indicator displays green (which can take up to 1 minute) the process is complete and the camera has been reset.

Open ports
----------
 * 80: web interface
 * 554: H.264 video stream (RTSP)

To Check
--------
Will the camera will get a DHCP address if it is connected to a network with an accessible DHCP server?

Is port 443 open for HTTPS?
