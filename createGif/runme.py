# only edit SCALE_FACTOR to make screen smaller or bigger
import pygame
from PIL import Image
from editme import main
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import importlib
from time import sleep

WIDTH = 32
HEIGHT = 7
SCALE_FACTOR = 20
        
pygame.init()
dspSize = (WIDTH * SCALE_FACTOR, HEIGHT * SCALE_FACTOR)
screen = pygame.display.set_mode(dspSize)
frames = []
durations = []
running = True
restart = False
clock = pygame.time.Clock()
surface32x7 = pygame.Surface((WIDTH, HEIGHT))
font = pygame.font.Font('./MatrixChunky6X.ttf', 7)  # Default font, size 36

screen.fill((0, 0, 0)) 
surface32x7.fill((0, 0, 0)) 


def render(delay=20, isExport=False):
    d = delay if delay >= 20 else 20
    if running and not restart:
        scaled_surface = pygame.transform.scale(surface32x7, dspSize)
        screen.blit(scaled_surface, (0, 0))  
        pygame.display.flip()
        
        if isExport:
            frame_data = pygame.surfarray.array3d(surface32x7)
            frames.append(Image.fromarray(frame_data.transpose(1, 0, 2))) 
            durations.append(d)
        
        clock.tick(1000/d) 


def clear():
    surface32x7.fill((0, 0, 0))
        
def drawPixel(position, color):
    surface32x7.set_at(position, color)

def drawText(text, pos, color):
    text = font.render(text, True, color)
    surface32x7.blit(text, pos)
    return text.get_width()

def marquee(text, color, sep, isExport, delay=20):
    twidth = drawText(text, (0,0), color)
    for i in range(twidth + sep):
        drawText(text, (-i,0), color)
        drawText(text, (twidth+sep-i,0), color)
        render(delay, isExport)
        clear()
         
         
def handle_events():
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

def export():
    main(pygame, render, drawPixel, drawText, marquee, clear, surface32x7, 32, 7, True)
    frames[0].save('animation.gif', save_all=True, append_images=frames[1:], duration=durations, loop=0)
    pygame.quit()    
     
                
if __name__ == '__main__':
    
    class MyHandler(FileSystemEventHandler):
        def on_modified(self, event):
            try:
                global main
                global restart
                import editme
                importlib.reload(editme)
                restart = True
                main = editme.main
            except Exception as e:
                print(e)
                
    observer = Observer()
    observer.schedule(MyHandler(), path="./editme.py", recursive=False)
    observer.start()

    event_thread = threading.Thread(target=handle_events)
    event_thread.start()

    while running:
        surface32x7.fill((0, 0, 0))
        try:
            main(pygame, render, drawPixel, drawText, marquee, clear, surface32x7, 32, 7, False)
        except Exception as e:
            print(e)
        restart = False
    
    event_thread.join()
    observer.stop()
    observer.join()
    pygame.quit()
