# pygame - a pygame class instance you can use to draw shapes and just use it as you would in any pygame application, read the pygame docs or tutorials
# render - ONE RENDER IS ONE GIF FRAME, call this function like this: render(isExport) to render the scene, ignore isExport
# drawPixel((x,y), (r,g,b)) - fill a pixel with color
# drawText(str, (x,y), (r,g,b)) - draw text
# marquee(str, (r,g,b), sep, isExport) - animating text from right to left in a loop, sep is the width between the reappearing text, ignore isExport 
# clear() - clears the screen
# surface - the surface pygame draws on, example usage: surface.fill((0, 0, 0)), this clears the screen
# width, height - 32x7, its the resolution of the led matrix
# isExport - ignore

def main(pygame, render, drawPixel, drawText, marquee, clear, surface, width, height, isExport):
    
    #for y in range(height):
    #    for x in range(width):
    #        drawPixel((x,y), (240,0,0))
    #        render(17, isExport)
    
    marquee('Tami is DA BEST !!! <3 <3 <3', (0,250,0), 4, isExport, 70)