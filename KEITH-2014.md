---
layout: page
title: KEITH (2014)
---

## KEITH's Development

### A little baby robot...

KEITH MK1 started out as a Raspberry Pi with a PiRoCon motor control board, a HC-SR04 ultrasonic module, two cheap 6v DC motors, an RC car battery and a Tamiya track set, base board and double gearbox. Control was through a Wiimote using its bluetooth to connect to the PI?
![KEITH MK1](http://keiththerobot.uk/images/MK1.JPG "KEITH MK1")

Nothing too complicated happened at this stage of development but programming started to get the ultrasonic distance sensor working. To start with, I used code from <a href="https://github.com/chrisalexander/initio-pirocon-test/blob/master/sonar.py">here</a> which sends out a pulse to the ultrasonic sensor, then times how long that pulse takes to get back. This time, when used with the speed of sound, can give you a fairly accurate reading of how far away any object is.

The biggest problem we had with this was just that - it was fairly accurate, and due to the non-real-time nature of the Raspberry Pi we sometimes had some hugely anomalous results. To avoid this particular problem, later in development I put the results in a rolling list and took the median, so any bad results would be filtered out as either too high or too low. The only problem with this approach was that it introduced a slight delay in readings.

MK1a had only one large change - KEITH gained an eye! I had an official Raspberry Pi camera lying around, so I decided to stick it on with some masking tape. It took a while to get working properly, but eventually I had an MJPEG stream 'working' at about 2fps...
![KEITH MK1a](http://keiththerobot.uk/images/MK1a.jpg "KEITH MK1a")

### Starting to grow up

With KEITH MK2 came a completely new track configuration, which involved moving the gearbox on top of the baseplate. Along with that, a block of wood was added so the battery was balanced. All this time it was still held together with velcro...

The new track layout meant that turning was a lot faster as there was no longer the friction of the whole track spinning on the floor. The new angled front also helped with climbing over obstacles.
![KEITH MK2](http://keiththerobot.uk/images/MK2.JPG "KEITH MK2")

### Some new clothes

MK3 was the first iteration of KEITH with a proper chassis, which was made out of 3mm plywood and cut with a jigsaw... Needless to say, it wasn't quite a masterpiece yet, but it certainly did the job until we could get the MK4 chassis laser cut.

![KEITH MK3](http://keiththerobot.uk/images/MK3.JPG "KEITH MK3")

### Lasers!

The patterns for the new MK4 chassis parts were created using AutoCad - a programme used by Dad at work. We happened to be going to a Makerfest in Halifax and one of the exhibitors was a local company selling laser cutters. They advertised that they would cut parts for free if files were in .dxf format (the cad direct exchange format). So we took a memory stick with us and came away with a full set parts ready to go! The accuracy of our MK4 chassis  made a huge difference and we were able to start to refine the chassis to fit everything in and work out how to make things accessible. Space in this little bot was tight!

![KEITH MK4](http://keiththerobot.uk/images/MK4.JPG "KEITH MK4")

MK5  was our final iteration and had a removeable top to allow the battery to be removed without disturbing the nest of wires. By this time as well as the ultrasonic sensor on the front, KEITH sported a line following sensor, wheel encoders and a number of leds, including one laser... The camera remained but was not needed for PiWars. We also created a couple of attachments that fitted onto the front of KEITH for two of the challenges.

### PIWARS 2014



<a href="http://www.raspberrypi.org">Raspberry Pi</a> is a trademark of the Raspberry Pi Foundation.
