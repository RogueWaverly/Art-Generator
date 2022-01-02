from PIL import Image, ImageDraw
from colors import colors
import random

length = 512
black = colors['black']
periwinkle = colors['periwinkle']
white = colors['white']
min_width = 10
max_width = 40

def bg_gradient(index, i, j):
  bg_list = [
    (
      periwinkle[0]+(length//2-j)//2,
      periwinkle[1]+(i-j)//3,
      periwinkle[2]+(length//2-i)//4,
    ),
    (
      periwinkle[0]+(length//2-i)//2,
      periwinkle[1]+(i-j)//3,
      periwinkle[2]+(length//2-j)//4,
    ),
    (
      periwinkle[0]+(length//2-i)//2,
      periwinkle[1]+(length//2-j)//3,
      periwinkle[2]+(i-j)//4,
    ),
  ]

  return bg_list[index%len(bg_list)]

img = Image.new('RGB', (length, length), black)

pixels = img.load()
prev_left_x = 0
prev_right_x = 0
left_x = int(random.random()*max_width)+min_width
right_x = int(left_x + random.random()*max_width)+min_width
up = True
index = 0
while right_x < length:
  left_y = prev_right_y = length if up else 0
  right_y = prev_left_y = 0 if up else length
  for i in range(prev_left_x, right_x):
    for j in range(length):
      if (up and \
          (j-left_y)*(right_x-left_x) <= (i-left_x)*(right_y-left_y) and \
          (j-prev_left_y)*(prev_right_x-prev_left_x) <= (i-prev_left_x)*(prev_right_y-prev_left_y)) or \
          (not up and \
          (j-left_y)*(right_x-left_x) >= (i-left_x)*(right_y-left_y) and \
          (j-prev_left_y)*(prev_right_x-prev_left_x) >= (i-prev_left_x)*(prev_right_y-prev_left_y)):
        pixels[i, j] = bg_gradient(index, i, j)
  prev_left_x = left_x
  prev_right_x = right_x
  left_x = int(right_x + random.random()*max_width)+min_width
  right_x = int(left_x + random.random()*max_width)+min_width
  up = not up
  index += 1

left_y = prev_right_y = length if up else 0
right_y = prev_left_y = 0 if up else length
for i in range(prev_left_x, length):
  for j in range(length):
    if (up and \
        0 <= (i-length)*(right_y-left_y) and \
        (j-prev_left_y)*(prev_right_x-prev_left_x) <= (i-prev_left_x)*(prev_right_y-prev_left_y)) or \
        (not up and \
        0 >= (i-length)*(right_y-left_y) and \
        (j-prev_left_y)*(prev_right_x-prev_left_x) >= (i-prev_left_x)*(prev_right_y-prev_left_y)):
      pixels[i, j] = bg_gradient(index, i, j)

draw = ImageDraw.Draw(img)
def draw_snowflake(x, y):
  size = 5
  draw.line((x-size+2, y-size, x+size-2, y+size), fill=white)
  draw.line((x+size-2, y-size, x-size+2, y+size), fill=white)
  draw.line((x-size, y, x+size, y), fill=white)

for i in range(0, length, 63):
  for j in range(0, length, 63):
    x = i+random.random()*50-25
    y = j+random.random()*50-25
    draw_snowflake(x, y)

img.save("Inktober/04-FREEZE.png", "PNG")
