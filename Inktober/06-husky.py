from PIL import Image, ImageDraw
from colors import colors
import random
import math

length = 512
periwinkle = colors['periwinkle']
canary = colors['canary']
white = colors['white']
buff = length//64

bg_radius_wide = length//128
bg_radius_high = bg_radius_wide*4
corn_radius_wide = bg_radius_wide*6
corn_radius_high = bg_radius_high*6
corn_center_x = length//2
corn_center_y = length//3*2

def husk(x, y):
  lime = colors['lime']
  return (
    lime[0]-y+int(corn_radius_high/3*2*math.cos((x-corn_center_x)/corn_radius_wide*4/3)+corn_center_y-corn_radius_high/2),
    lime[1]-y+int(corn_radius_high/3*2*math.cos((x-corn_center_x)/corn_radius_wide*4/3)+corn_center_y-corn_radius_high/2),
    lime[2]-y+int(corn_radius_high/3*2*math.cos((x-corn_center_x)/corn_radius_wide*4/3)+corn_center_y-corn_radius_high/2),
  )

def inner_husk(x, y):
  lime = colors['lime']
  return (
    lime[0]-y+int(corn_radius_high/3*2*math.cos((x-corn_center_x)/corn_radius_wide*4/3)+corn_center_y-corn_radius_high/4),
    lime[1]-y+int(corn_radius_high/3*2*math.cos((x-corn_center_x)/corn_radius_wide*4/3)+corn_center_y-corn_radius_high/4),
    lime[2]-y+int(corn_radius_high/3*2*math.cos((x-corn_center_x)/corn_radius_wide*4/3)+corn_center_y-corn_radius_high/4),
  )

def corn(x, y):
  return (
    canary[0]+(10*x%corn_radius_high)-(10*y%corn_radius_high),
    canary[1]+(10*x%corn_radius_high)-(10*y%corn_radius_high),
    canary[2]+(10*x%corn_radius_high)-(10*y%corn_radius_high),
  )

def sky(x, y):
  return (
    periwinkle[0]+1-((x-corn_center_x)**2//bg_radius_wide**2+(y-corn_center_y)**2//bg_radius_high**2)//2,
    periwinkle[1]+1-((x-corn_center_x)**2//bg_radius_wide**2+(y-corn_center_y)**2//bg_radius_high**2)//15,
    periwinkle[2]+1-((x-corn_center_x)**2//bg_radius_wide**2+(y-corn_center_y)**2//bg_radius_high**2)//20,
  )

img = Image.new('RGB', (length, length), periwinkle)

pixels = img.load()

for x in range(length):
  for y in range(length):
    if y > corn_radius_high/3*2*math.cos((x-corn_center_x)/corn_radius_wide*3/2)+corn_center_y+corn_radius_high/7 and \
        y < corn_radius_high/3*2*math.cos((x-corn_center_x)/corn_radius_wide*5/4)+corn_center_y+corn_radius_high/5*2 and \
        y < -((x-corn_center_x)/corn_radius_wide*3)**2+corn_center_y+corn_radius_high*5/4:
      pixels[x, y] = husk(x, y)
    elif y < -1/8*(x-corn_center_x)**2+corn_center_y+corn_radius_high and \
        y > -1/4*(x-corn_center_x)**2+corn_center_y+corn_radius_high and \
        y > -1/15*(x-corn_center_x)**2+corn_center_y+corn_radius_high/8:
      pixels[x, y] = inner_husk(x, y)
    elif ((x-corn_center_x)**2/corn_radius_wide**2+(y-corn_center_y)**2/corn_radius_high**2) < 1:
      pixels[x, y] = corn(x, y)
    else:
      pixels[x, y] = sky(x, y)

draw = ImageDraw.Draw(img)

popcorn_radius_1 = 5
kernel_radius = 2
popcorn_radius_2 = 3
popcorn_radius_3 = 2
def draw_popcorn(x, y):
  kernel_x = random.randint(x-popcorn_radius_1, x+popcorn_radius_1)
  kernel_y = random.randint(y-popcorn_radius_1, y+popcorn_radius_1)
  popcorn_x_2 = random.randint(x-popcorn_radius_1, x+popcorn_radius_1)
  popcorn_y_2 = random.randint(y-popcorn_radius_1, y+popcorn_radius_1)
  popcorn_x_3 = random.randint(x-popcorn_radius_1, x+popcorn_radius_1)
  popcorn_y_3 = random.randint(y-popcorn_radius_1, y+popcorn_radius_1)
  draw.ellipse((x-popcorn_radius_1, y-popcorn_radius_1, x+popcorn_radius_1, y+popcorn_radius_1), fill=white)
  draw.ellipse((kernel_x-kernel_radius, kernel_y-kernel_radius, kernel_x+kernel_radius, kernel_y+kernel_radius), fill=colors['red'])
  draw.ellipse((popcorn_x_2-popcorn_radius_1, popcorn_y_2-popcorn_radius_1, popcorn_x_2+popcorn_radius_1, popcorn_y_2+popcorn_radius_1), fill=white)
  draw.ellipse((popcorn_x_3-popcorn_radius_1, popcorn_y_3-popcorn_radius_1, popcorn_x_3+popcorn_radius_1, popcorn_y_3+popcorn_radius_1), fill=white)

for x in range(0, length, 64):
  for y in range(0, length, 64):
    if ((x-corn_center_x)**2/(corn_radius_wide*3)**2+(y-corn_center_y)**2/(corn_radius_high*1.5)**2) > 1:
      popcorn_x_1 = random.randint(x-length//16, x+length//16)
      popcorn_y_1 = random.randint(y-length//16, y+length//16)
      draw_popcorn(popcorn_x_1, popcorn_y_1)

img.show()
img.save("Inktober/06-HUSKY.png", "PNG")
