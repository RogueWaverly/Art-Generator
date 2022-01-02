from PIL import Image
from colors import colors
import math

length = 512
white = colors['white']
blue = colors['taiwan-blue']
red = colors['taiwan-red']
periwinkle = colors['periwinkle']

def x_length(angle, hypotenuse):
  return math.sin(math.radians(angle))*hypotenuse

def y_length(angle, hypotenuse):
  return math.cos(math.radians(angle))*hypotenuse

sun_point_angle = 30
num_points = 12
sun_center_x = length//4
sun_center_y = length//3
sun_spacing = length//120
sun_point_outer_radius = sun_spacing*15
sun_point_inner_radius = sun_spacing*17//2
sun_circle_radius = sun_spacing*15//2

img = Image.new('RGB', (length, length), blue)
pixels = img.load()

sun_points = []
for point_index in range(num_points):
  angle_from_center = 360//num_points*point_index
  sun_points.append({
    'angle_from_center': angle_from_center,
    'point_x': int(sun_center_x+x_length(90-angle_from_center, sun_point_outer_radius)),
    'point_y': int(sun_center_y+y_length(90-angle_from_center, sun_point_outer_radius)),
    'left_slope': math.tan(math.radians(angle_from_center-180+sun_point_angle/2)),
    'right_slope': math.tan(math.radians(angle_from_center-180-sun_point_angle/2)),
    'cut_slope': math.tan(math.radians(angle_from_center-90)),
    'reflect_left': 90 <= angle_from_center < 270,
    'reflect_right': 90 < angle_from_center <= 270,
    'reflect_cut': 180 < angle_from_center <= 360,
  })

def is_sun_point(x, y):
  for point in sun_points:
    if (
        (
          (not point['reflect_left'] and y >= point['left_slope']*(x-point['point_x']) + point['point_y']) or
          (point['reflect_left'] and y <= point['left_slope']*(x-point['point_x']) + point['point_y'])
        ) and
        (
          (not point['reflect_right'] and y <= point['right_slope']*(x-point['point_x']) + point['point_y']) or
          (point['reflect_right'] and y >= point['right_slope']*(x-point['point_x']) + point['point_y'])
        ) and
        (x-sun_center_x)**2 + (y-sun_center_y)**2 >= sun_point_inner_radius**2 and
        (
          (point['reflect_cut'] and y <= point['cut_slope']*(x-sun_center_x) + sun_center_y) or
          (not point['reflect_cut'] and y >= point['cut_slope']*(x-sun_center_x) + sun_center_y)
        )):
      return True
  return False

def bg(x, y):
  return (
    periwinkle[0]+(length//2-x)//2,
    periwinkle[1]+(length//2-x)//3,
    periwinkle[2]+(length//2-x)//4,
  )

for x in range(length):
  for y in range(length):
    if ((x-sun_center_x)**2 + (y-sun_center_y)**2 < sun_circle_radius**2 or
        is_sun_point(x, y)):
      pixels[x, y] = white
    elif y <= length//6 or y >= length//6*5:
      pixels[x, y] = bg(x, y)
    elif x >= length//2 or y >= length//2:
      pixels[x, y] = red

img.show()
img.save("Inktober/10-PATTERN.png", "PNG")
