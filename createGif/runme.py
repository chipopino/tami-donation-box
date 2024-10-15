import pygame
from PIL import Image
from editme import main
import threading

WIDTH = 32
HEIGHT = 7
SCALE_FACTOR = 30

pygame.init()
dspSize = (WIDTH * SCALE_FACTOR, HEIGHT * SCALE_FACTOR)
screen = pygame.display.set_mode(dspSize)
frames = []
running = True
clock = pygame.time.Clock()
surface32x7 = pygame.Surface((WIDTH, HEIGHT))

screen.fill((0, 0, 0)) 
surface32x7.fill((0, 0, 0)) 

def drawPixel(position, color):
    surface32x7.set_at(position, color)

def render(isExport=False):
    scaled_surface = pygame.transform.scale(surface32x7, dspSize)
    screen.blit(scaled_surface, (0, 0))  
    pygame.display.flip()
    
    if isExport:
        frame_data = pygame.surfarray.array3d(surface32x7)
        frames.append(Image.fromarray(frame_data.transpose(1, 0, 2))) 
    
    clock.tick(60) 

def export():
    main(pygame, render, drawPixel, surface32x7, 32, 7, True)
    frames[0].save('animation__0.1__.gif', save_all=True, append_images=frames[1:], duration=20, loop=0)
    pygame.quit()
    
if __name__ == '__main__':
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        surface32x7.fill((0, 0, 0)) 
        main(pygame, render, drawPixel, surface32x7, 32, 7, False)
    pygame.quit()
