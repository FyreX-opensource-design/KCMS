# KCMS
klipper config managment system

not much to be said here (yet), but here's what's down.

we use this git repo for managing macros that aren't hosted on git servers and get to retrieve them. Links are provided in their config files.
for those that are we just do a git pull from their repos, but this depends widely on the repo how we do it.
we store a copy of every config that's installed in the /klipper/config folder, which is cleaned and given a .gitignore flag upon running install.py so that future updates to Klipper don't fill it. The kinematics folder is also cleared and any python files installed compiled to .pyc
everything is numbered as follows.

1: kinematics
2: Z axis setups
3: probes
4: buckets and wipers
5: macros

they can be selected like the following examples (after running kcms.py)

121 (for 2WD coreXY) or 21 (for the ERCF)
