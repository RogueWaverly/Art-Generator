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

min_ring = length//32
max_ring = length//8
min_rotate  = 30
max_rotate = 60
rings = []
radius = random.randint(min_ring, max_ring)
angle = random.randint(0, 360)
while radius <= math.sqrt(2*(length/2)**2):
  rings.append({
    'radius': radius,
    'angle': angle,
  })
  radius += random.randint(min_ring, max_ring)
  angle += random.randint(min_rotate, max_rotate)   
  angle = 360%angle
rings.append({
  'radius': radius,
  'angle': angle,
})

min_angle = 30
max_angle = 60
min_offset = -50
max_offset = 50
start_slice = random.randint(0, 360)
slice_angle = 0
offset_x = random.randint(min_offset, max_offset)
offset_y = random.randint(min_offset, max_offset)
slices = []
while slice_angle < 360:
  slices.append({
    'angle': start_slice + slice_angle,
    'offset_x': offset_x,
    'offset_y': offset_y,
  })
  slice_angle += random.randint(min_angle, max_angle)
  offset_x = random.randint(min_offset, max_offset)
  offset_y = random.randint(min_offset, max_offset)

for sl in slices:
  sl['angle'] %= 360
slices = sorted(slices, key=lambda k: k['angle'])

center_x = length//2
center_y = length//2

def get_angle(x, y):
  for ring in rings:
    if ring['radius'] >= math.sqrt((x-center_x)**2+(y-center_y)**2):
      return ring['angle']

def get_offsets(x, y):
  slice_center_x = x-center_x
  slice_center_y = y-center_y
  for slice_index in range(len(slices)):
    left_slice = slices[slice_index]
    right_slice = slices[(slice_index+1)%len(slices)]
    current_angle = math.degrees(math.atan2(slice_center_y, slice_center_x))
    current_angle += 180
    if current_angle > left_slice['angle'] and \
        current_angle < right_slice['angle']:
      return left_slice['offset_x'], left_slice['offset_y']
  return slices[-1]['offset_x'], slices[-1]['offset_y']

def magic(x, y):
  start_angle = get_angle(x, y)
  offset_x, offset_y = get_offsets(x, y)
  center_x = length/2
  center_y = length/2
  radius = length/4
  subradius = length/16
  diffuse = length
  return (
    white[0]-int((x-(center_x+offset_x+x_length(start_angle, radius)))**2 + (y-(center_y+offset_y+y_length(start_angle, radius)))**2 - subradius**2)//diffuse,
    white[1]-int((x-(center_x+offset_x+x_length(start_angle+120, radius)))**2 + (y-(center_y+offset_y+y_length(start_angle+120, radius)))**2 - subradius**2)//diffuse,
    white[2]-int((x-(center_x+offset_x+x_length(start_angle+240, radius)))**2 + (y-(center_y+offset_y+y_length(start_angle+240, radius)))**2 - subradius**2)//diffuse,
  )

img = Image.new('RGB', (length, length), white)

pixels = img.load()

for x in range(length):
  for y in range(length):
    pixels[x, y] = magic(x, y)

draw = ImageDraw.Draw(img)

img.show()
img.save("Inktober/08-FRAIL.png", "PNG")
