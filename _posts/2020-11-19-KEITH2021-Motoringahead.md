---
layout: post
title: Motoring Ahead
categories: [KEITH, K2021]
image: http://keiththerobot.uk/images/k2021-motors.jpg
---

In this post we look at our new motors and early thoughts on control. It’s a short post!

KEITH Evo was propelled by a couple of 12 volt 25mm diameter motors with integral 100rpm gearboxes. He had loads of torque (pulling power) but wasn’t particularly quick. With the ‘extended’ obstacle course in PiWars At Home we thought a bit more speed might be in order…  As always, Harry spent some time researching ideas and finally found some 12 volt motors sold to power beetle-weight combat robots. They are a slightly smaller diameter that the originals but fit comfortable within the same space and have the same shafts – meaning that the original drive wheels for the tracks still fit. 

The motors are rated to 900rpm! This results in lower torque, so the initial concern was that they would not be able to turn KEITH on his tracks. Beetle-weight robots are up to 1.5kg in weight, so we reasoned that they would work given that KEITH Evo only weighed around 1kg. Some testing was in order.

The brackets for the original motors were not suitable for the new ones so a couple of iterations of 3d printed brackets were produced and tried. The first was too lightweight and flexed badly. The second worked well but the motor positioning wasn’t quite right (we were using the original mounting holes on the chassis) so a third was produced and then a second copy for the other motor. Why orange plastic? It was what Harry had in the printer and it won’t be seen anyway! It was nice to see KEITH wearing his tracks again!


![KEITH2021 Motors](http://keiththerobot.uk/images/k2021-motors.jpg "New Motors")

Harry had bought a pair of motor controllers that were matched to the motors so they were hooked up and attached directly to the radio control receiver. This allowed KEITH to be controlled using one stick on the transmitter per motor (think tank-style control). Not only is this a very difficult way of driving a model, but it also proved that KEITH will be much quicker that he was – and we only used about 30% power on the 3 cell LiPo battery (about 11 volts), He was also able to turn easily on lino, carpet and the back door mat. When necessary, we can use the 4 cell LiPo battery for turbo boost!

KEITH Evo used the radio with an small arduino circuit translating instructions from the radio receiver into something that the PI could use to then control the motors. This allowed Harry to ‘mix’ the signals so that one stick on the transmitter controlled forward, backward, left and right proportionally, making KEITH Evo relatively easy and intuitive to control. The next stage of the build will be to replicate that arrangement using the new motor controllers a Teensy LC microcontroller (to replace the arduino) and our lovely new Pi4. The motor power circuit will be protected using a suitable UBEC.
