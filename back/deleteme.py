from PIL import Image
from rpi_ws281x import PixelStrip, Color
import time

LED_COUNT = 32*7
LED_PIN = 18   
TIME_PER_GIF_IN_SEC = 10

def rgba_to_rgb(pixel):
    alpha = pixel[3] / 255.0
    new_r = int(pixel[0] * alpha)
    new_g = int(pixel[1] * alpha)
    new_b = int(pixel[2] * alpha)
    return (new_r, new_g, new_b)

def readGif(fileName):
    gif = Image.open(fileName)  
    frame_number = gif.n_frames  
    frames = []

    for i in range(1, frame_number):
        gif.seek(i)  
        frame_data = list(gif.getdata())
        frame = []
        for y in range(gif.height):
            col = []
            for x in range(gif.width):
                col.append(rgba_to_rgb(frame_data[x + y*gif.width]))
            frame.append(col)
                
        frames.append(frame)  
        
    return frames

def playGif(fileName):
    frames = readGif(fileName)
    strip = PixelStrip(LED_COUNT, LED_PIN)
    start_time = time.time()
    
    while time.time() - start_time < TIME_PER_GIF_IN_SEC:
        for f in frames:
            i = 0
            strip.begin()
            for y in f:
                for x in y:
                    strip.setPixelColor(i, Color(x[0], x[1], x[2]))
                    i += 1
            strip.show()
            time.sleep(0.1)
    
if __name__ == '__main__':
    playGif('/mnt/gifs/gifs/NewPiskel.gif')
