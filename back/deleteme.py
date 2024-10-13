from PIL import Image
from rpi_ws281x import PixelStrip, Color
import time
import re

LED_COUNT = 3
LED_PIN = 18   
TIME_PER_GIF_IN_SEC = 10
MIN_ALLOWED_DELAY_PER_GIF = 0.01

def clear_strip(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))  
    strip.show()


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
    
    for i in range(0, frame_number):
        gif.seek(i)  
        frame_data = list(gif.convert("RGBA").getdata())
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
    
    delay = 0.1
    try:
        delay = float(re.search(r'(?<=__)\d(\.\d+?)?(?=__)', fileName).group())
        if delay < MIN_ALLOWED_DELAY_PER_GIF:
            delay = MIN_ALLOWED_DELAY_PER_GIF
    except Exception as e:
        print(e)
        pass
    
    while time.time() - start_time < TIME_PER_GIF_IN_SEC:
        for f in frames:
            i = 0
            strip.begin()
            for y in f:
                for x in y:
                    strip.setPixelColor(i, Color(x[0], x[1], x[2]))
                    i += 1
            strip.show()
            time.sleep(delay)
    
    clear_strip(strip)
    
if __name__ == '__main__':
    try:
        strip = PixelStrip(LED_COUNT, LED_PIN)
        #strip.begin()  # Initialize the strip
        #strip.setPixelColor(0, Color(0, 255, 0))
        #strip.show()
        print("LED strip initialized successfully.")
        #playGif('/mnt/gifs/gifs/NewPiskel__0.01__.gif')
    except Exception as e:
        print("AAAAAAAAAAAAAAAA", e)
