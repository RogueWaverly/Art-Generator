from PIL import Image, ImageDraw
from colors import colors, random_color
import random

img = Image.new('RGB', (512,512), 'black')

pixels = img.load()
for i in range(img.size[0]):
  for j in range(img.size[1]):
    pixels[i,j] = (colors["periwinkle"][0]+(i-j)//2, colors["periwinkle"][1]+(i-j)//3, colors["periwinkle"][2]+(i-j)//4)

draw = ImageDraw.Draw(img)
for i in range(0, img.size[0], 50):
  for j in range(0, img.size[1], 50):
    upper = random.random()*50-20
    lower = random.random()*50+20
    draw.ellipse((i+upper, j+upper, i+lower, j+lower), outline=random_color())

img.save("RING", "PNG")
