---
layout: page
title: KEITH (2014)
---

## KEITH's Development

### A little baby robot...

KEITH MK1 started out as a Raspberry Pi with a PiRoCon motor control board, a HC-SR04 ultrasonic module, two cheap 6v DC motors, an RC car battery and a Tamiya track set, base board and double gearbox.
![KEITH MK1](http://keiththerobot.uk/images/MK1.JPG "KEITH MK1")

Nothing too complicated happened at this stage of development but programming started to get the ultrasonic distance sensor working. To start with, I used code from <a href="https://github.com/chrisalexander/initio-pirocon-test/blob/master/sonar.py">here</a> which sends out a pulse to the ultrasonic sensor, then times how long that pulse takes to get back. This time, when used with the speed of sound, can give you a fairly accurate reading of how far away any object is.

The biggest problem we had with this was just that - it was fairly accurate, and due to the non-real-time nature of the Raspberry Pi we sometimes had some hugely anomalous results. To circumnavigate this particular problem, later in development I added a rolling median, so any bad results would be filtered out as either too high or too low.

MK1a had only one large change - KEITH gained an eye! I had an official Raspberry Pi camera lying around, so I decided to stick it on with some masking tape. It took a while to get working properly, but eventually I had an MJPEG stream 'working' at about 2fps...
![KEITH MK1a](http://keiththerobot.uk/images/MK1a.jpg "KEITH MK1a")

### Starting to grow up

With KEITH MK2 came a complete new track configuration, which involved moving the gearbox on top of the baseplate. Along with that, a block of wood was added so the battery was balanced. All this time it was still held together with velcro...
![KEITH MK2](http://keiththerobot.uk/images/MK2.JPG "KEITH MK2")

### Some new clothes

MK3 was the first iteration of KEITH with a proper chassis, which was made out of 3mm plywood and cut with a jigsaw... Needless to say, it wasn't quite a masterpiece yet but it certainly did the job until we could get the MK4 chassis laser cut.


<a href="http://www.raspberrypi.org">Raspberry Pi</a> is a trademark of the Raspberry Pi Foundation.
