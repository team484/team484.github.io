---
layout: default
title: Raspberry Pi Camera
categories: [ hardware, public]
tags: [ camera, vision, raspberrypi]
---

[home page](http://www.raspberrypi.org/camera) - on raspberrypi.org

[documentation](RaspiCamDocs.pdf) - (PDF) [github source](https://github.com/raspberrypi/userland/blob/master/host_applications/linux/apps/raspicam/RaspiCamDocs.odt)

Note: the example commands didn't work for me until I switch the version of netcat from `nc.openbsd` to `nc.traditional`:

	sudo update-alternatives --config nc