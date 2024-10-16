# pygame - a pygame class instance you can use to draw shapes and just use it as you would in any pygame application, read the pygame docs or tutorials
# render(delay, isExport) - 
#   ONE RENDER IS ONE GIF FRAME, 
#   call this function like this: render(<delay in milliseconds>, isExport) to render the scene, 
#   the delay is the number of milliseconds the animation while halt untill the next frame
#   ignore isExport  
# drawPixel((x,y), (r,g,b)) - fill a pixel with color
# drawText(str, (x,y), (r,g,b)) - draw text
# marquee(str, (r,g,b), sep, isExport) - animating text from right to left in a loop, sep is the width between the reappearing text, ignore isExport 
# clear() - clears the screen
# surface - the surface pygame draws on, example usage: surface.fill((0, 0, 0)), this clears the screen
# width, height - 32x7, its the resolution of the led matrix
# isExport - ignore

def main(pygame, render, drawPixel, drawText, marquee, clear, surface, width, height, isExport):
    
    # ~~ simple example ~~
    #for y in range(height):
    #    for x in range(width):
    #        drawPixel((x,y), (240,0,0))
    #        render(20, isExport)
    
    # ~~ coins ~~
    # for x in range(75):
    #     clear()
    #     pygame.draw.polygon(surface, (0,250,0), [(x-5,0), (x-5,6), (3+x-5,3)])
        
    #     for c in range(4):
    #         pygame.draw.circle(surface, (250,250,0), (-10+x-c*9,3), 3)
        
    #     render(40, isExport)
        
    # ~~ marquee ~~
    marquee('Tami is DA BEST !!! <3 <3 <3', (0,250,0), 4, isExport, 70)
    

