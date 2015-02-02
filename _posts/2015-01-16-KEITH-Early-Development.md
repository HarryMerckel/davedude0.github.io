---
layout: post
title: KEITH MK1
categories: [KEITH,hidden]
---

## KEITH's Early Development

PiWars was the primary driving force behind KEITH's development, as it gave us a goal to make KEITH for. We needed to make a robot that could navigate 

## KEITH as a little baby robot...

KEITH MK1 started out as a Raspberry Pi with a PiRoCon motor control board, a HC-SR04 ultrasonic module, two cheap 6v DC motors, an RC car battery and a Tamiya track set, base board and double gearbox. (I will insert links to parts and prices here)
![image](http://keiththerobot.uk/images/MK1.JPG "KEITH MK1")
Nothing too complicated happened at this stage of development but programming started to get the ultrasonic distance sensor working. To start with, I used code from <a href="https://github.com/chrisalexander/initio-pirocon-test/blob/master/sonar.py">here</a> which sends out a pulse to the ultrasonic sensor, then times how long that pulse takes to get back. This time, when used with the speed of sound, can give you a fairly accurate reading of how far away any object is.
The biggest problem we had with this was just that - it was fairly accurate, and due to the non-real-time nature of the Raspberry Pi we sometimes had some hugely anomalous results. To circumnavigate this particular problem, later in development I added a rolling median, so any bad results would be filtered out as either too high or too low.
MK1a had only one large change - KEITH gained an eye! I had an official Raspberry Pi camera lying around, so I decided to stick it on with some masking tape. It took a while to get working properly, but eventually I had an MJPEG stream 'working' at about 2fps...


<a href="http://www.raspberrypi.org">Raspberry Pi</a> is a trademark of the Raspberry Pi Foundation.

