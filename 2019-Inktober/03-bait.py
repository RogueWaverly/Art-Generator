from PIL import Image, ImageDraw
from colors import colors
import random
import math

length = 512
black = colors['black']
periwinkle = colors['periwinkle']
white = colors['white']
center_i = length//3
center_j = length//3
small_radius = 32
large_radius = 128

img = Image.new('RGB', (length, length), black)

pixels = img.load()
for i in range(length):
  for j in range(length):
    # orb
    if ((i-center_i)**2 + (j-center_j)**2) < small_radius**2:
      pixels[i, j] = (
        periwinkle[0]+((i-center_i)**2 + (j-center_j)**2 - small_radius**2)//4,
        periwinkle[1]+((i-center_i)**2 + (j-center_j)**2 - small_radius**2)//6,
        periwinkle[2]+((i-center_i)**2 + (j-center_j)**2 - small_radius**2)//8
      )
    # radiance
    else:
      pixels[i, j] = (
        periwinkle[0]-((i-center_i)**2 + (j-center_j)**2 - large_radius**2)//400,
        periwinkle[1]-((i-center_i)**2 + (j-center_j)**2 - large_radius**2)//600,
        periwinkle[2]-((i-center_i)**2 + (j-center_j)**2 - large_radius**2)//800
      )

draw = ImageDraw.Draw(img)

def draw_star(x, y):
  height = 4.5
  width = 0.5
  draw.ellipse((x-width, y-height, x+width, y+height), fill=white)
  draw.ellipse((x-height, y-width, x+height, y+width), fill=white)

for i in range(0, img.size[0], 63):
  for j in range(0, img.size[1], 63):
    # more stars
    if ((i-center_i)**2 + (j-center_j)**2) > (2*large_radius)**2:
      x = i+random.random()*50-25
      y = j+random.random()*50-25
      draw_star(x, y)
      x = i+random.random()*50
      y = j+random.random()*50
      draw_star(y, x)
    # fewer stars
    elif ((i-center_i)**2 + (j-center_j)**2) > large_radius**2:
      x = i+random.random()*50-25
      y = j+random.random()*50-25
      draw_star(x, y)
    # else no stars

img.save("Inktober/03-BAIT.png", "PNG")
