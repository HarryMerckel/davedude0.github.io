---
layout: page
title: KEITH (2014)
---

## KEITH's Development

### A little baby robot...

KEITH MK1 started out as a Raspberry Pi with a PiRoCon motor control board, a HC-SR04 ultrasonic module, two cheap 6v DC motors, an RC car battery and a Tamiya track set, base board and double gearbox. Control was through a Wiimote using its bluetooth to connect to the PI.
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

The patterns for the new MK4 chassis parts were created using AutoCad - a programme used by Dad at work. We happened to be going to a Makerfair in Halifax and one of the exhibitors was a local company selling laser cutters. They advertised that they would cut parts for free if files were in .dxf format (the cad direct exchange format). So we took a memory stick with us and came away with a full set parts ready to go! The accuracy of our MK4 chassis  made a huge difference and we were able to start to refine the chassis to fit everything in and work out how to make things accessible. Space in this little bot was tight!

![KEITH MK4 Schematic](http://keiththerobot.uk/images/Mk4-schematic.JPG "KEITH MK4 Schematic")

![KEITH MK4 Parts](http://keiththerobot.uk/images/MK4-parts.JPG "KEITH MK4 Parts")

![KEITH MK4](http://keiththerobot.uk/images/MK4.JPG "KEITH MK4")

### Putting It All Together

MK5  was our final iteration and had a removeable top to allow the battery to be removed without disturbing the nest of wires. By this time as well as the ultrasonic sensor on the front, KEITH sported a line following sensor, wheel encoders, a capacitance switch (emergency stop!) and a selection of leds, including one laser... The camera remained but was not needed for PiWars. the motors/gearbox was tilted back to create enough space to put a small circuit board in with an expansion chip so that the leds could be operated through just two gpio pins on the Pi. We also created a couple of attachments that fitted onto the front of KEITH for two of the challenges, one using servos to operate a ball-catcher and catapult.

![KEITH MK5](http://keiththerobot.uk/images/DSC04940-adjusted--web.jpg "KEITH MK5")

![KEITH MK5 BACK](http://keiththerobot.uk/images/DSC04938-adjusted-web.jpg "KEITH MK5 Back")

![KEITH MK5 GOLF MODULE](http://keiththerobot.uk/images/DSC04942-adjusted-web.jpg "KEITH MK5 Golf Module")

![KEITH MK5 SUMO MODULE](http://keiththerobot.uk/images/DSC04941-adjusted-web.jpg "KEITH MK5 Sumo Module")

### PIWARS 2014

This competition took place on 4 December 2014 in Cambridge. On the day there were 21 competing teams. The event consisted of 7 physical challenges and 4 judged. Points were awarded for performance in each challenge with bonuses awarded for completing some challenges autonomously.

### 1. ROBOT GOLF

AIM: Collect a ball from the spot and move it forwards then push it through a mousehole in the wall. Timed. Remote control.

RESULT: Attachment to collect and hold ball worked well, catapult not so good. 8th out of 16 competitors.

### 2. PROXIMITY

AIM: Move from a point towards a wall and stop as close to it as possible. Penalties for touching the wall. Autonomous.

RESULT: Two good runs and one where KEITH turned and one corner touched the wall. 9th out of 16 competitors.

### 3. STRAIGHT LINE SPEED TEST

AIM: To run along a 7m long course as fast as possible without touching the sides. Controlled or autonomous.

RESULT: Three decent autonomous runs. 3rd out of 18 competitors.

### 4. THREE POINT TURN

AIM: To carry out a three point turn, passing fixed points and returning to the original position. Timed. Autonomous.

RESULT: Our most frustrating challenge! KEITH failed to do what he was programmed to do, twice! We incurred maximum penalties as a result. Having reset everything, KEITH proceeded to do a perfect run (ADD YOUTUBE LINK). 13th out of 13 competitors.

### 5. OBSTACLE COURSE

AIM: To traverse a series of obstacles. Timed. Controlled.

RESULT: More frustration! KEITH negotiated the pebbles without slowing, but failed to get over the wooden blocks. Harry tried several times before we realised that one drive wheel had slipped off its shaft and was not turning. We took the penalty and pushed the wheel back home. KEITH completed the slalom and see-saw without issue. 11th out of 20 competitors.

### 6. LINE FOLLOWER

AIM: To follow a black line on a white background and to complete as many laps as possible in a set time. Autonomous.

RESULT: KEITH was accurate and steady producing five clean laps. Not as fast as a couple of others. 3rd out of 8 competitors.

### 7. SUMO

AIM: To push another robot of the arena.

RESULT: We had a series of 'byes' and by the time we got to compete we were up against winners of previous rounds that were much bigger than KEITH? We lost quickly!

### 8. CODE QUALITY

Harry's code was submitted for assessment and was judged on quality and structure. KEITH was judged to be 7= out of 19 competitors.

### 9. AESTHETICS

This was a subjective judgement and KEITH was 12th out of 24 robots judged.

### 10. MOST INNOVATIVE AND 11. MOST FEATURE RICH

Results for these two categories were not published...

### OVERALL RESULTS

BEST AUTONOMOUS ROBOT: 3rd of 21 robots.

BEST REMOTE-CONTROLLED ROBOT: 13th of 21 robots.

BEST ROBOT OVER £75: 3rd of 10 robots.

### CONCLUSIONS

We had a mixed bag of results with some very good events and a couple of disappointments. We thought that our main problem was being consistent and reliable. However, third in the autonomous challenges and third in class overall was, we thought, a very respectable result for our first robot and first competition.

<a href="http://www.raspberrypi.org">Raspberry Pi</a> is a trademark of the Raspberry Pi Foundation.
