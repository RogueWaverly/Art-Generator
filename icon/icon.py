from PIL import Image, ImageColor
import math


def rgb_gradient(width, height, x, y):
  base_color = ImageColor.getrgb('#FFFFFFFF')

  center_x = width/2
  center_y = height/2

  x_radius = width/4
  y_radius = height/4

  start_angle = 30

  length = max(width, height)
  diffuse = length*3

  def x_length(angle):
    return math.sin(math.radians(angle))*x_radius

  def y_length(angle):
    return math.cos(math.radians(angle))*y_radius

  return (
    base_color[0] - round(
        (x - (center_x + x_length(start_angle)))**2
        + (y - (center_y + y_length(start_angle)))**2
      ) // diffuse,
    base_color[1] - round(
        (x - (center_x + x_length(start_angle + 120)))**2
        + (y-(center_y + y_length(start_angle + 120)))**2
      ) // diffuse,
    base_color[2] - round(
        (x - (center_x + x_length(start_angle + 240)))**2
        + (y-(center_y + y_length(start_angle + 240)))**2
      ) // diffuse,
  )


icon = Image.open('chrysanthemum.png')
i_width, i_height = icon.size
width = max(icon.size)
height = width

img = Image.new('RGBA', (width, height), 'white')

pixels = img.load()
for x in range(width):
  for y in range(height):
    pixels[x, y] = rgb_gradient( width, height, x, y )

i_x = (width - i_width)//2
i_y = (height - i_height)//2
img.paste(icon, (i_x, i_y), icon)

img.save('icon.png', 'PNG')
