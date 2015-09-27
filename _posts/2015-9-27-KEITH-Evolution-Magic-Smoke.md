---
layout: post
title: KEITH Evolution - Magic Smoke...
categories: [KEITH, evo]
---

A lot of progress has been made with getting control systems in place and electronics put together, and I even got to the point of making the motors move but all did not go to plan...

So, a bit of background. So far I have an arduino decoding the signal from the RC receiver and feeding it to the Raspberry Pi over the USB connection, which works rather well to say that I'm interfacing between modern, 25 year old and 35 year old technology.
Separately, we tested the motors by hooking them up directly to a battery pack, which also worked well - it went in a pretty straight line to say that the batteries were rattling around loose and there was no control.
Then came the connection between the two - I designed and built a small motor control board with a 5v switching regulator and a SN75441ONE quadruple half-h driver all connected together on a breadboard  with a couple of ceramic capacitors. In theory it should support voltages from 7 to 36 and brief currents of up to 2A per channel, well above the rated 0.24A of the motors. I decided that, at first, I wanted to test without the regulator - I think it's always best to make sure everything works separately before connecting it all together. At first it worked perfectly well, with motors spinning and no obvious problems, after which we sat down for dinner.

After a nice meal I plugged things back in, including the regulator this time, and started testing again to check my code for converting the radio control axes into differential drive for the motors worked. After a short amount of (incredibly fast, come to think of it) motor spinning the SN75441ONE decided that it was a great time to release some magic smoke! Suffice to say that it didn't work after that - I still need to work out what caused the problem, but without a good multimeter that may be hard. The next circuit will probably be based on something I know can support those currents, not just based off the data sheets and google searches!

~Harry
