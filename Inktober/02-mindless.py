from PIL import Image, ImageDraw
from colors import colors
import random

img = Image.new('RGB', (512,512), 'black')

pixels = img.load()
for i in range(img.size[0]):
  for j in range(img.size[1]):
    pixels[i,j] = (colors["periwinkle"][0]+(171-j)//2, colors["periwinkle"][1]+(171-j)//3, colors["periwinkle"][2]+(171-j)//4)

draw = ImageDraw.Draw(img)
draw.line((0, 171, 512, 171), fill=colors["white"])

for i in range(0, img.size[0], 40):
  j = 5
  increment = 18
  while j < 171:
    left = random.random()*20-5
    right = random.random()*20+5
    draw.line((i-left, j, i+right, j), fill=colors["white"], width=3)
    j += increment
    increment -= 1

for i in range(64, img.size[0], 64):
  draw.line(((256-i)*1.5+256, 512, 300, 171), fill=colors["white"])

draw.chord((112, 121, 212, 221), start=180, end=0, fill=colors["white"])

img.save("Inktober/02-MINDLESS.png", "PNG")
