# use this directory to create gifs for the led matrix to display

usage:
```bash
pip3 install Pillow pygame watchdog
python3 runme.py
```
this while open a window with the resulting gif playing.  
edit editme.py and see the change take place in the window.  
you can change SCALE_FACTOR in runme.py to change screen size.  

## after creating the gif:
```bash
python3 export.py
```

change the __0.1__ part of the exported gif name to other numbers, this is the time in seconds that is added to each frame as a delay, so small numbers result in a faster animation

upload the resulting gif to ipOfTheRaspbarrypi/index.html
