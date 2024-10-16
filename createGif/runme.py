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
running = True
restart = False
clock = pygame.time.Clock()
surface32x7 = pygame.Surface((WIDTH, HEIGHT))
font = pygame.font.Font('./MatrixChunky6X.ttf', 7)  # Default font, size 36

screen.fill((0, 0, 0)) 
surface32x7.fill((0, 0, 0)) 

def drawPixel(position, color):
    surface32x7.set_at(position, color)

def clear():
    surface32x7.fill((0, 0, 0))
    
def drawText(text, pos, color):
    text = font.render(text, True, color)
    surface32x7.blit(text, pos)
    return text.get_width()

def marquee(text, color, sep, isExport):
    twidth = drawText(text, (0,0), color)
    for i in range(twidth + sep):
        drawText(text, (-i,0), color)
        drawText(text, (twidth+sep-i,0), color)
        render(isExport)
        clear()
        sleep(0.05)
         
def render(isExport=False):
    if running and not restart:
        scaled_surface = pygame.transform.scale(surface32x7, dspSize)
        screen.blit(scaled_surface, (0, 0))  
        pygame.display.flip()
        
        if isExport:
            frame_data = pygame.surfarray.array3d(surface32x7)
            frames.append(Image.fromarray(frame_data.transpose(1, 0, 2))) 
        
        clock.tick(60) 

def export():
    main(pygame, render, drawPixel, drawText, marquee, clear, surface32x7, 32, 7, True)
    frames[0].save('animation__0.1__.gif', save_all=True, append_images=frames[1:], duration=20, loop=0)
    pygame.quit()

def handle_events():
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
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
