# use this directory to create gifs for the led matrix to display

## usage
pip3 install Pillow pygame watchdog
python3 runme.py

then edit editme.py to change the resulting gif

## after creating the gif:
python3 export.py

change the __0.1__ part of the gif name to other numbers, this is the time in seconds that is added to each frame as a delay, so small numbers result in a faster animation

upload the resulting gif to <ipOfTheRaspbarrypi>/index.html