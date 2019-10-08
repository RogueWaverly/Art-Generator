from PIL import Image, ImageDraw
from colors import colors
import random
import math

length = 512
white = colors['white']

def x_length(angle, hypotenuse):
  return math.sin(math.radians(angle))*hypotenuse

def y_length(angle, hypotenuse):
  return math.cos(math.radians(angle))*hypotenuse

def magic(x, y):
  center_x = length/2
  center_y = length/2
  radius = length/4
  start_angle = 30
  subradius = length/16
  diffuse = length
  return (
    white[0]-int((x-(center_x+x_length(start_angle, radius)))**2 + (y-(center_y+y_length(start_angle, radius)))**2 - subradius**2)//diffuse,
    white[1]-int((x-(center_x+x_length(start_angle+120, radius)))**2 + (y-(center_y+y_length(start_angle+120, radius)))**2 - subradius**2)//diffuse,
    white[2]-int((x-(center_x+x_length(start_angle+240, radius)))**2 + (y-(center_y+y_length(start_angle+240, radius)))**2 - subradius**2)//diffuse,
  )

img = Image.new('RGB', (length, length), white)

pixels = img.load()

horizon = length//3
river_x = length//2

for x in range(length):
  for y in range(length):
    if x > -y+(y-horizon)*math.sin(y/(length/32))+2*river_x-length/32 and \
        x < y+(y-horizon)*math.sin(y/(length/32))+length/32 and \
        y >= horizon:
      pixels[x, y] = white
    elif y > length/3*math.sin((x-length/4)/length*2)+length/4+6 and \
        y < length/3*math.sin((x-length/4)/length*2)+length/4+10:
      pixels[x, y] = white
    elif y > length/3*math.sin((x+length/5*3+25)/length*2)+length/4+6 and \
        y < length/3*math.sin((x+length/5*3+25)/length*2)+length/4+10 and \
        y < length/3*math.sin((x-length/4)/length*2)+length/4+6:
      pixels[x, y] = white
    else:
      pixels[x, y] = magic(x, y)

draw = ImageDraw.Draw(img)

petal_radius = 3
def draw_flower(flower_center_x, flower_center_y, layers):
  flower_radius = petal_radius
  draw.ellipse(
    (
      flower_center_x-flower_radius,
      flower_center_y-flower_radius,
      flower_center_x+flower_radius,
      flower_center_y+flower_radius
    ),
    outline=white
  )
  for layer in range(layers):
    num_petals = int(math.pi*flower_radius/petal_radius)
    offset_angle = random.randint(0,360)
    for petal in range(num_petals):
      petal_angle = 360/num_petals*petal+offset_angle
      petal_center_x = flower_center_x + x_length(petal_angle, flower_radius)
      petal_center_y = flower_center_y + y_length(petal_angle, flower_radius)
      draw.arc(
        (
          petal_center_x-petal_radius,
          petal_center_y-petal_radius,
          petal_center_x+petal_radius,
          petal_center_y+petal_radius
        ),
        start=-petal_angle,
        end=-petal_angle+180,
        fill=white
      )
    flower_radius += petal_radius

flower_layers_1 = 5
flower_layers_2 = 4
flower_layers_3 = 3
flower_center_x_1 = length//4
flower_center_y_1 = length//5*2
flower_center_x_2 = flower_center_x_1-flower_layers_1*petal_radius-flower_layers_2*petal_radius-flower_layers_3*petal_radius
flower_center_y_2 = flower_center_y_1-flower_layers_2*petal_radius
flower_center_x_3 = (flower_center_x_1+flower_center_x_2)//2+flower_layers_3*petal_radius
flower_center_y_3 = flower_center_y_2-flower_layers_1*petal_radius
draw_flower(flower_center_x_1, flower_center_y_1, flower_layers_1)
draw_flower(flower_center_x_2, flower_center_y_2, flower_layers_2)
draw_flower(flower_center_x_3, flower_center_y_3, flower_layers_3)

sun_center_x = length//3*2
sun_center_y = length//4
sun_radius = 40
draw.ellipse((sun_center_x-sun_radius, sun_center_y-sun_radius, sun_center_x+sun_radius, sun_center_y+sun_radius), fill=white)

img.show()
img.save("Inktober/07-ENCHANTED.png", "PNG")
