from random import randint
from PIL import Image

img = Image.new(mode = "RGB", size = (4000,4000))
pixels = img.load()
points = [(0,0),(2000, 3464),(3999,0)]

pixels[points[0][0], points[0][1]] = (255,255,0)
pixels[points[1][0], points[1][1]] = (255,255,0)
pixels[points[2][0], points[2][1]] = (255,255,0)

colours = [(255,0,0), (0,255,0), (0,0,255)]

randInt = 0
newX = points[2][0]
newY = points[2][1]
for x in range(100000):
    newX = round((newX + points[randInt][0])/2)
    newY = round((newY + points[randInt][1])/2)

    pixels[newX, newY] = (newX % 255, newY % 255, 100)
    
    randInt = randint(0,2)

img.show()
img.save("triangle.png")
