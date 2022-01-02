from PIL import Image, ImageDraw
from colors import colors
import random

length = 512
periwinkle = colors['periwinkle']
red = colors['red']
buff = length//64

near_cloud_base_width = random.randint(length//20*3, length//6-buff)
near_cloud_height = near_cloud_base_width//8
near_cloud_base_x = random.randint(length//5-buff, length//5+buff)
near_cloud_base_y = random.randint(5*near_cloud_height+buff, length//4)
near_cloud_top_width = near_cloud_base_width//3*2
near_cloud_top_x = random.randint(near_cloud_base_x-near_cloud_base_width//6, near_cloud_base_x+near_cloud_base_width//6)
near_cloud_top_y = near_cloud_base_y-near_cloud_height

far_cloud_base_width = random.randint(int(near_cloud_base_width*1.5), near_cloud_base_width*2)
far_cloud_height = far_cloud_base_width//8
far_cloud_base_x = random.randint(near_cloud_base_x+length//8, near_cloud_base_x+length//7)
far_cloud_base_y = near_cloud_top_y-near_cloud_height
far_cloud_top_width = far_cloud_base_width//3*2
far_cloud_top_x = random.randint(far_cloud_base_x-far_cloud_base_width//6, far_cloud_base_x+far_cloud_base_width//6)
far_cloud_top_y = far_cloud_base_y-far_cloud_height

moon_radius = 10
moon_x = random.randint(length//6*5, length-moon_radius-buff)
moon_y = random.randint(moon_radius+buff, length//4-moon_radius)
cut_moon_radius = moon_radius*1.1
cut_moon_x = moon_x-moon_radius//5*3

def sky(i, j):
  if (i-near_cloud_base_x)**2/near_cloud_base_width**2 + (j-near_cloud_base_y)**2/near_cloud_height**2 < 1 or \
      (i-near_cloud_top_x)**2/near_cloud_top_width**2 + (j-near_cloud_top_y)**2/near_cloud_height**2 < 1:
    return (
      red[0]-(near_cloud_base_y+length//64-j)*3,
      red[1]-(near_cloud_base_y+length//64-j)*3,
      red[2]-(near_cloud_base_y+length//64-j)*3,
    )
  elif (i-far_cloud_base_x)**2/far_cloud_base_width**2 + (j-far_cloud_base_y)**2/far_cloud_height**2 < 1 or \
      (i-far_cloud_top_x)**2/far_cloud_top_width**2 + (j-far_cloud_top_y)**2/far_cloud_height**2 < 1:
    return (
      red[0]-(far_cloud_base_y+length//16-j)*3,
      red[1]-(far_cloud_base_y+length//16-j)*3,
      red[2]-(far_cloud_base_y+length//16-j)*3,
    )
  elif ((i-moon_x)**2 + (j-moon_y)**2) < moon_radius**2 and \
      ((i-cut_moon_x)**2 + (j-moon_y)**2) > cut_moon_radius**2:
    return red
  else:
    return (
      periwinkle[0]-(length//3*2-j)//2,
      periwinkle[1]-(length-j)//3,
      periwinkle[2]-(length-j)//4,
    )

def sunset(i, j):
  center_i = length//2
  center_j = 3*length//4
  radius = 32
  return (
    red[0]-(3*length//4-j)//3,
    red[1]-((i-center_i)**2 + (j-center_j)**2 - radius**2)//600,
    red[2]-((i-center_i)**2 + (j-center_j)**2 - radius**2)//5,
  )

def shadow(i, j):
  return (
    red[0]-(length-j)//4,
    red[1]-(length-j)//3,
    0,
  )

img = Image.new('RGB', (length, length), periwinkle)

pixels = img.load()

buildings = []

left_x = random.randint(buff, 2*buff)
corner_x = random.randint(length//10-buff, length//10+buff)
right_x = random.randint(length//5-2*buff, length//5-buff)
height = random.randint(length//2-2*buff, length//2)
buildings.append((left_x, corner_x, right_x, height))

left_x = random.randint(length//5+buff, length//5+2*buff)
corner_x = random.randint(length//10*3-buff, length//10*3+buff)
right_x = random.randint(length//5*2-2*buff, length//5*2-buff)
height = random.randint(length//2, length//2+2*buff)
buildings.append((left_x, corner_x, right_x, height))

left_x = random.randint(length//5*2+buff, length//5*2+2*buff)
corner_x = random.randint(length//15*8-buff, length//15*8+buff)
right_x = random.randint(length//3*2-2*buff, length//3*2-buff)
height = random.randint(length//9-buff, length//9+buff)
buildings.append((left_x, corner_x, right_x, height))

left_x = random.randint(length//3*2+buff, length//3*2+2*buff)
corner_x = random.randint(length//6*5-buff, length//6*5+buff)
right_x = random.randint(length-2*buff, length-buff)
height = random.randint(length//3-buff, length//3+buff)
buildings.append((left_x, corner_x, right_x, height))


slope_up = -1/3
slope_down = 1/3
index = 0
building = buildings[index]
for i in range(length):
  if i > building[2]:
    index += 1
    if index < len(buildings):
      building = buildings[index]
  for j in range(length):
    if building[0] <= i < building[1] and \
        j-building[3] > slope_up*(i-building[1]):
      pixels[i, j] = shadow(i, j)
    elif building[1] <= i < building[2] and \
        j-building[3] > slope_down*(i-building[1]):
      pixels[i, j] = sunset(i, j)
    else:
      pixels[i, j] = sky(i, j)

img.save("Inktober/05-BUILD.png", "PNG")
