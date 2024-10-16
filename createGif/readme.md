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

## important
try to minimize the uploading or deletion of gifs to the raspbarrypi server.  
the pis os is on a read only partition, so is the partition to which the gifs are uploaded, when a gif is uploaded or deleted, it first remounts the fs as read+write and after changes back to read only. this is to prevent corruption on sudden power loss.  
so to avoid damage from manny fs remounts, minimize upload or delete of gifs.
