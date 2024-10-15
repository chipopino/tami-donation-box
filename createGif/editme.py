# pygame - a pygame class instance you can use to draw shapes and just use it as you would in any pygame application, read the pygame docs or tutorials
# render - call this function like this: render(isExport) to render the scene
# drawPixel - convenience function to fill a pixel with color
# surface - the surface pygame draws on, example usage: surface.fill((0, 0, 0)), this clears the screen
# width, height - 32x7, its the resolution of the led matrix
# isExport - ignore

def main(pygame, render, drawPixel, surface, width, height, isExport):
    for x in range(width):
        for y in range(height):
            drawPixel((x,y), (50,0,0))
            render(isExport)
