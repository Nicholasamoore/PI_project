Basic Board Setup - MW
======================

Preamble
--------

I initially started this project by attempting to extract an image directly to the raspberry PI. There are a number of images available from raspberrypi.org. I did this with the opposite of a healess setup, connected to my TV with keyboard and mouse. I found etcher which improved the situation and lead to what our honoroed professor, Roie Black, referenced in an email to our class regarding headless setup.

Headless and VNC
----------------

-Headless Setup Guide: http://frederickvandenbosch.be/?p=2385

This guide gives the fastest method of getting up and running in the least amount of time. The next step for me, being at the time slightly less familiar with Linux than I am now, was to figure out how to get some kind of remote desktop style service that could allow me to remote in from wherever I was. There are a number of solutions out there, one offered on raspberrypi.org, real vnc, seemed to offer a litany of pay type choices which did not appeal to me. That's where tight vnc came in to the picture.

-Tight VNC Guide: https://www.raspberrypi.org/forums/viewtopic.php?f=49&t=50698

This was handy but ultimately not very useful. Though, as I am not aware of a command line configuration tool for my home router, this has been effective in managing port forwarding and other settings from a remote site.

Raspberry PI Location
---------------------

One of the things that you realize almost immediately is that it is just so darn inconvenient to have the PI with you, needing to connect to the same network as any host you are using to remote in. This prompted me to hang our group PI from a router on my home network. Thus far, it has allowed each member of the group to reach the PI via SSH reliably.

Commands
--------

-Tight VNC: open vnc://our.ip.xxx.xxx:5901 (tight vnc port is 5901, configured for our purposes to be forwarded there from another port)

-SSH: ssh -p <port> pi@our.ip.xxx.xxx (replace <port> with port that forwards to 22 on network)

-SCP: scp -P <port> file.to.transfer pi@our.ip.xxx.xxx:home/pi/...
