from PIL import Image, ImageDraw
from colors import colors
import random
import math

length = 512
black = colors['black']
red = colors['red']
white = colors['white']

def sunset(x, y):
  return (
    red[0]-(length//3*2-y)//4*3,
    red[1]-(length//8*7-y)//4*3,
    red[2]-length//8-y//5,
  )

img = Image.new('RGB', (length, length), black)

pixels = img.load()

horizon = length//3
river_x = length//2

swing_center_x = length//6
swing_center_y = length//3
swingset_height = length//6
swingset_width = length//8
swingset_slope = 8
swing_length = swingset_height//5*4
swing_width = swingset_width//3

moon_radius = 10
moon_x = length//4*3
moon_y = length//5
cut_moon_radius = moon_radius*1.1
cut_moon_x = moon_x-moon_radius//5*3

for x in range(length):
  for y in range(length):
    if x > -y+(y-horizon)*math.sin(y/(length/32))+2*river_x-length/32 and \
        x < y+(y-horizon)*math.sin(y/(length/32))+length/32 and \
        y >= horizon:
      pixels[x, y] = black
    elif y > length/3*math.sin((x-length/4)/length*2)+length/4+6 and \
        y < length/3*math.sin((x-length/4)/length*2)+length/4+10:
      pixels[x, y] = black
    elif y > length/3*math.sin((x+length/5*3+25)/length*2)+length/4+6 and \
        y < length/3*math.sin((x+length/5*3+25)/length*2)+length/4+10 and \
        y < length/3*math.sin((x-length/4)/length*2)+length/4+6:
      pixels[x, y] = black
    elif y >= -swingset_slope*(x-swing_center_x-swingset_width//2+1)+swing_center_y+1 and \
        y <= -swingset_slope*(x-swing_center_x-swingset_width//2-1)+swing_center_y-1 and \
        swing_center_y < y < swing_center_y+swingset_height:
      pixels[x, y] = black
    elif y <= swingset_slope*(x-swing_center_x-swingset_width//2+1)+swing_center_y-1 and \
        y >= swingset_slope*(x-swing_center_x-swingset_width//2-1)+swing_center_y+1 and \
        swing_center_y < y < swing_center_y+swingset_height:
      pixels[x, y] = black
    elif y >= -swingset_slope*(x-swing_center_x+swingset_width//2+1)+swing_center_y+1 and \
        y <= -swingset_slope*(x-swing_center_x+swingset_width//2-1)+swing_center_y-1 and \
        swing_center_y < y < swing_center_y+swingset_height:
      pixels[x, y] = black
    elif y <= swingset_slope*(x-swing_center_x+swingset_width//2+1)+swing_center_y-1 and \
        y >= swingset_slope*(x-swing_center_x+swingset_width//2-1)+swing_center_y+1 and \
        swing_center_y < y < swing_center_y+swingset_height:
      pixels[x, y] = black
    elif y >= swing_center_y-1 and \
        y <= swing_center_y+1 and \
        swing_center_x-swingset_width//2 < x < swing_center_x+swingset_width//2:
      pixels[x, y] = black
    elif x == swing_center_x-swing_width//2 and \
        swing_center_y < y < swing_center_y+swing_length:
      pixels[x, y] = black
    elif x == swing_center_x+swing_width//2 and \
        swing_center_y < y < swing_center_y+swing_length:
      pixels[x, y] = black
    elif y >= swing_center_y+swing_length-1 and \
        y <= swing_center_y+swing_length+1 and \
        swing_center_x-swing_width//2 < x < swing_center_x+swing_width//2:
      pixels[x, y] = black
    elif ((x-moon_x)**2 + (y-moon_y)**2) < moon_radius**2 and \
        ((x-cut_moon_x)**2 + (y-moon_y)**2) > cut_moon_radius**2:
      pixels[x, y] = white
    else:
      pixels[x, y] = sunset(x, y)

draw = ImageDraw.Draw(img)

img.show()
img.save("Inktober/09-SWING.png", "PNG")
