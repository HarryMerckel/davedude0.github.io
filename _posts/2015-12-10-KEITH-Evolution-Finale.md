---
layout: post
title: So, How Did We Do?
categories: [KEITH, evo]
---

Saturday 5th December 2015 was an early start. We hit the road for the journey from Leeds to Cambridge at 06:02, heading for the A1 south in driving rain and blustery winds. A short stop for breakfast and coffee as the sun came up left us ready for the final hours driving and we rolled into the car park of the William Gates Building shortly after 09:00. There were signs, so we knew we were in the right place!

Directed to Pit Room B, we set our stuff up and went out to explore the courses before the doors opened to spectators. Everything was set up and waiting, all looking very professional with lots of cheerful Jam Makers and Judges on hand. The obstacle course looked incredible with its shiny turntable. The marble obstacle was a cause of concern! There were many murmurs about the line following course – tight bends, an over 90 degree angled turn and a narrow white strip either side of the line, as is the Cannybots trademark. It looked great, but very scary… We had been given a short piece of wire when we arrived so that we could ensure that our fixing for Pi Noon would work. It was now that we worked out what the challenge would be. Brilliant! Such an improvement on Sumo!

Back in the pit room it was great to meet up with Grahame (Gnasher 2), Richard (Averagebot) and Dave (Cybercondriac). We had been swapping notes and some mild abuse on Twitter in the months leading up to the competition – they are as much fun in real life as on line! We also met Finley with his marvellous meccano creation, Lobsang. We had been following his work from deepest Wales through his blog and he turned out to be the same age as Harry (the brain behind KEITH Evo). We dads will always do what we can for our kids, but a 4 ½ hour drive each way was definitely in the ‘above and beyond’ category!

So, we already had a great impression of this year’s event and set ourselves up to do some basic checks before our first event, the Skittles.

### Skittles

KEITH Evolution is armed… Under the front of the chassis is a ball catcher and set into the back of that is a small rubber band powered cannon. The cannon is fashioned from copper tube, copper sheet and piano wire soldered together using plumbers solder (lead-free, of course). The piston within it is a short length of steel tube (that once carried electrical wires within the walls of our house) that happened to be a good, loose, fit. A bolt, wing-nuts, a ball joint from a servo link wire and a washer completed that element. A rubber band each side provided the means of shooting the piston forward and it was all angled within the chassis to aim at the centre of the ball. The firing mechanism was a small servo with an arm that locked through the washer on the piston. When the switch on the RC transmitter was flicked, the servo pulled the pin and the cannon fired. All great in theory… Reloading has to be done manually so the Pi was mounted on a ply board that was hinged so it could be lifted up and forward to give access without disturbing wires.

![Ball catcher and cannon](http://keiththerobot.uk/images/Evo-catcher.png "Ball catcher and cannon")

The ball-catcher and cannon.

![Cannon trigger](http://keiththerobot.uk/images/Evo-trigger.png "Cannon trigger")

The firing mechanism with the Pi tilted up.

We arrived at the challenge and the judge explained the rules. We loaded the cannon and did a test fire – nothing! Great start – not. A quick check revealed that we had pulled a servo wire off its pin. That was pushed back home and all was well again. The technique needed was quite delicate and we had not practised with a ball of the same weight. The art was to keep the ball at the back of the catcher,ërr which was harder than it looked, to aim and then fire the cannon BEFORE stopping/reversing before the fault line.
Our first shot was good – four or five skittles. The second shot was weak. I fired after I had started to decelerate and the cannon was not very effective. The third shot was good but I went over the fault line. The remaining shots were lacklustre and we came away with a score of 11 skittles.

### Proximity

Lessons had been learned from 2014 for this challenge. We knew we needed to be close, but more important was to avoid earning any penalties. The front of Keith is wide and flat, so on the approach to the wall any slight turn would mean that the track could hit the wall when the sensor was telling KEITH that he was still not close enough. An attachment was crafted that provided a point at the front and also gave a minimum distance well above the minimum that could be measured by the SR04 ultrasonic unit we used.

![Proximity add-on](http://keiththerobot.uk/images/Evo-prox.png "Proximity add-on")

The code was set so that KEITH slowed as he approached the wall, crawling the final few cm. The SR04 has a tendency to give ‘odd’ readings so Harry got round that by taking the median of sets of five readings (thus excluding excessively large or small distances). Even then the final distance from the wall had a range of a few millimetres. We did a quick check on the corridor outside the pit room and KEITH hit the wall on the second attempt! Harry adjusted the ‘stop’ dimension by a millimetre and he behaved himself.

Off down to the challenge and KEITH did his stuff. The LEDs worked, the lasers worked and our results were 3.5mm, 1.5mm and 2mm giving a total distance of 7mm! We were very chuffed with that!

### Line Follower

KEITH Evo uses the Ryanteck line follower sensor which is set into the bottom of the chassis just in front of the centre of turn of the robot (full forward on one track and full backwards on the other makes KEITH Evo spin on the spot – the centre of turn).

![Underside](http://keiththerobot.uk/images/Evo-under.png "Underside")

We had time before this challenge to swap the batteries and check KEITH Evo out on our test track .Harry’s code has a general speed variable which makes it easy to set the maximum speed of the motors for each challenge. The line follower sometimes loses the track at higher speeds  but we decided to stick with full speed and to cross our fingers!

Off we went and the judge outlined the rules again (5 laps, max 5 minutes, one free rescue per lap and other rescues earned a penalty). We decided to place KEITH Evo just after that horrible angled turn and hope for the best. The video speaks for itself…

<iframe width="560" height="315" src="https://www.youtube.com/embed/qhU_4ken0EI" frameborder="0" allowfullscreen></iframe>

Our hearts were in our mouths as KEITH Evo reached the final turn of the first lap and went a little wide. He turned gently back towards the line, found it, wiggled a little and kept going. Frankly, we could not believe it. Harry had added a bit of code last week to allow KEITH to ‘remember’ where the line was if all sensors were reading white and to turn back towards that side. We had experimented with the rate of turn for that and were not completely convinced! KEITH Evo then proceeded to complete the five laps without an issue. We were VERY pleased!

### 3 Point Turn

No doubt the hardest challenge is the three point turn. The requirements are simple: drive forward, turn, forward, reverse, forward, turn, forward and stop. How hard can that be? Well, making our tracked bot drive in a straight line is not so easy. Making him turn predictably also not easy. The variables that we found were the state of the batteries, the floor surface, the motors, the grip of the tracks and whether there is an ‘r’ in the month!

We had decided to work on dead-reckoning using encoders on the drive wheels. We used a pair of polulu reflectance sensors and made black and white discs for the back of the wheels. Harry spent some time getting everything working and then we had to calibrate it to get the number of ‘ticks’ per metre of travel. A quick and dirty calculation gave us a starting point and then we adjusted the number of ticks in the programme to establish a constant and repeatable metre. Once we had that, we were able to input the distances needed for the three point turn and work out the ticks on each wheel to get him to turn 90degrees. The code was structured to allow this to be easily adjusted as different floors produced different turn rates. We had also tried ways of comparing the ticks on each side to adjust motor speed to make KEITH Evo run in a straight line. We had such variable results that we decided to just calibrate the robot and fix a differential on the forward speed to achieve a straight line.

![Wheel encoders](http://keiththerobot.uk/images/Evo-encoders.png "Wheel encoders")

Sensors and disc visible – just.

On the day we had half an hour to sort things out so we put another set of fresh batteries in and went into the corridor to do some checks on the hard floor. The first test run (using some settings set on our kitchen floor) was awful! The stone tiles were producing completely different characteristics to a smoother surface. We then tried KEITH on a table top. We tweaked a few things and set off for the challenge. Our first run was fine, but KEITH Evo missed the box on the return. A minor tweak and he then completed a clean run and missed the box, but on the other side! Another tiny adjustment and the third run worked. We thought we should have done better, but no penalties was the aim and we had succeeded there!

<iframe width="560" height="315" src="https://www.youtube.com/embed/4_uCfew41dE" frameborder="0" allowfullscreen></iframe>

### Straight Line Speed Test

The aim here was to use the wheel encoders to try to make KEITH Evo run straight. With 100rpm motors he was never going to be very fast, so the aim was to try to earn bonus points for being autonomous and not touching the sides. On the first run he hit the side fairly early on and travelled up the course running against the wall. Runs two and three were the same, despite minor adjustments to try to balance the motors better. The nice thing was that our speeds were remarkably consistent.

<iframe width="420" height="315" src="https://www.youtube.com/embed/GZNf4cbdIm8" frameborder="0" allowfullscreen></iframe>

### Pi Noon

We had just 10 minutes to swap batteries and check the radio control for our first challenge. We went up against a four wheel robot that was quicker than KEITH Evo, but didn’t turn quite as fast. The chase was quite short and an opportune turn burst our opponent’s balloon as they charged us. I felt really guilty that we had knocked our opponent out, but a little pleased that we had made it to round 2.

<iframe width="560" height="315" src="https://www.youtube.com/embed/-HXKfINi3Zo" frameborder="0" allowfullscreen></iframe>

Following Pi Noon we had a long break – time to recharge our own batteries, take a proper look at the other robots, visit the stands and watch some other challenges. The whole event felt well planned and relaxed. The traders and other exhibitors were all chatty and helpful. I was particularly impressed with Mohammed’s 3D printed tracks and wheels on his ir battling tank!

### Obstacle Course

New batteries (again) and a little more foam packing around the batteries to make sure they did not fall out set us up for this challenge. With our pretty loom band grip enhancers were were comfortable that KEITH Evo could get over the switchback. The marbles were a concern, but watching other bots suggested that they were fairly well down in their mounts so all we could do was hope. I had an idea of how to enter and exit the turntable of doom without getting trapped and the see-saw held little fear (famous last words…). Our proportional motor control through the joystick on the RC transmitter gave me as much control as I needed with smooth turns easy to achieve, so we set up on the start line.

The switchback was harder than anticipated. The first rise was very steep and I had to use the sides to get enough grip to get over the top. The dip was short enough for KEITH Evo to skip over and I made a confident turn towards the marbles. Full speed in a straight line left them all in place so it was on up the ramp to the turntable… A little adjustment on position and I made a clean entry between the barriers. So far so good. A couple of seconds to orientate myself (it's amazing how a rotating robot messes with your coordination!) and a quick exit with the barrier just catching the back of the robot on the way. Down the ramp at full speed, a smooth turn onto the see-saw and I thought I was home free. The see-saw tilted over without hesitation KEITH Evo was heading for the finish line. As the see-saw hit the floor under KEITH Evo’s weight, he stopped! All the lights were out. I looked at Harry who reported no connection. I lifted the battery pack and one AA battery had bounced off its connectors! We took the penalty because it would have taken longer to reboot everything. Gutted. We have not seen the results, but we think we were at about 45 seconds as we hit the see-saw… All I can say is that if something is going to go wrong, it will be the thing you did not foresee!

<iframe width="560" height="315" src="https://www.youtube.com/embed/6M8IfCv--Wo" frameborder="0" allowfullscreen></iframe>

We did a demo run a few minutes later which was not as smooth or fast, but proved that KEITH Evo is a versatile and manoeuvrable little robot.

A little later we went up against Optimus Pi, a four wheeled bot, in the second round of Pi Noon. We ran circles around each other for a few seconds, but he was faster and took us out with little problem. That was our competition over so we enjoyed watching the finals of Pi Noon, won by the amazing Triangula, and chatting with other competitors. It was pleasing that we had been knocked out by the second place bot!

### Prizes!

The last event of the day was the prize ceremony. Harry and I sat there with KEITH Evo. We really hoped we had done enough to win a challenge, but really had no idea. One of the joys of competing is that you really don't get a feel for how others are doing… Tim and Mike gave their thanks to the wonderful sponsors and the army of judges and Jam Makers. They were suitably embarrassed by the three cheers from the teams and audience, even though it was very well deserved.

The first event announced was the three point turn and KEITH Evo had won. Harry’s grin was set and his delight was clear. Aesthetics and blogging were announced and then we heard that KEITH Evo had won the line following too! Very chuffed!! Our friends with Gnasher2 won Jim Darby’s blinkiness award and Dave, with Cybercondriac, won the obstacle course. We were announced as being in second place for the proximity challenge with a total distance of 0.7cm until it was realised that the first place result had its decimal point in the wrong place. A quick check by Tim saw KEITH Evo promoted to first! Three challenges won! The tension as the overall winners of the A3 and A4 classes were announced left us with hearts beating fast. The awesome Pyrobot by Brian Corteil took the A3 class. We knew we were in the running for the A4 class but Hitchin Hackspace (with the rocket-powered straight line test and the only strike of the skittles competition fame) had also won three challenges. We were amazed and delighted to be called up as winners of the A4 class. PiWars Winner 2015!

![Winner!](http://keiththerobot.uk/images/Evo-winner.png "Winner!")



Finley, creator of Lobsang, asked about how we had fitted everything into KEITH Evolution. Here, just for you Finley, are a few pictures of KEITH Evo with his top off!



![Stripboard Transistors](http://keiththerobot.uk/images/Evo-transistors.png "Stripboard Transistors")

Stripboard circuits. This end has the transistors used for switching the LEDs. The red and blue wires are from the lasers. Hot-glue used to hold everything in place!



![Stripboard Resistors](http://keiththerobot.uk/images/Evo-resistors.png "Stripboard Resistors")

Part way down the stripboard and the resistors used to reduce the voltage of the signal from the ultrasonic sensor from 5v to 3v are visible.



![Buck regulator](http://keiththerobot.uk/images/Evo-buck.png "Buck regulator")

This is the little buck regulator from PiBorg to reduce the ~15v input to 5v for LED and sensor power. Capacitors to smooth things out.



![Top view](http://keiththerobot.uk/images/Evo-top1.png "Top view") ![Top view](http://keiththerobot.uk/images/Evo-top2.png "Top view")

The view from above..



![Arduino and Trigger](http://keiththerobot.uk/images/Evo-tilted.png "Arduino and Trigger")

The Pi tilted up to show the cannon and the radio receiver with its arduino on top. All wires around the moving parts of the cannon were glued into place to avoid any unfortunate entrapments… The red LEDs at the back are also visible.



![Battery bay](http://keiththerobot.uk/images/Evo-battery.png "Battery bay")

A final view across the battery bay. The motor controller chips with their heat-sinks are visible on the circuit board. The cannon barrel is visible at the bottom with the line follower sensor just below.

We’ve done a quick calculation of what KEITH Evolution cost this year. Including the Pi we have spent around £160. The radio control kit was donated and most of the laser cutting was free. I hate to think how many hours were spent designing, drawing, building, coding and testing...

### And Finally:-
All of Harry’s code for KEITH Evolution is at [https://github.com/davedude0/KEITH/tree/master/PiWars%202015](https://github.com/davedude0/KEITH/tree/master/PiWars%202015)
