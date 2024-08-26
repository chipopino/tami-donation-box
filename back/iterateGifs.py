from readGif import readGif
import os
from time import sleep
from rpi_ws281x import PixelStrip, Color

def playGif(file):
    frames = readGif(file)
    
    for f in range(len(frames)):
        for y in range(len(frames[f])):
            for x in range(len(frames[f][y])):
                print('frame, x, y, pixel: ', f, x, y, frames[f][y][x])
        print(f"that wase frame {f} of giif {file}")
        sleep(2)

for file in os.listdir('gifs'):
    playGif(os.path.join('gifs', file))
    sleep(3)

