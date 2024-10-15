def main(pygame, render, drawPixel, surface, width, height, isExport):
    for x in range(width):
        for y in range(height):
            drawPixel((x,y), (50,0,0))
            render(isExport)
