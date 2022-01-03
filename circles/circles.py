from PIL import Image, ImageColor, ImageDraw
from seeded_random import seeded_random 
import math


SEED = None
random = seeded_random( SEED )


FILENAME = "circles"

WIDTH = 600
HEIGHT = 600


NEUTRALS = {
  'black': ImageColor.getrgb( '#000000FF' ),
  'white': ImageColor.getrgb( '#FFFFFFFF' ),
}
WEDDING_PALETTE = {
  'plum': ImageColor.getrgb( '#301934FF' ),
  'sangria': ImageColor.getrgb( '#66023CFF' ),
  'prickly-pear': ImageColor.getrgb( '#A5134BFF' ),
  'grapefruit': ImageColor.getrgb( '#DC395DFF' ),
  'papaya': ImageColor.getrgb( '#F2684DFF' ),
}
PALETTE_1 = {
  '1-black': ImageColor.getrgb( '#1B262CFF' ),
  '1-navy': ImageColor.getrgb( '#0F4C75FF' ),
  '1-teal': ImageColor.getrgb( '#00B7C2FF' ),
  '1-orange': ImageColor.getrgb( '#FDCB9EFF' ),
}

def random_palette_color():
  return random.choice( list( WEDDING_PALETTE.values() ) + list( PALETTE_1.values() ) )


RING_TYPES = [
  {
    "range": ( 0, 1/3 ),
    "rings": ( 4, 7 ),
    "count": ( 1, 2 ),
  },
  {
    "range": ( 1/3, 2/3 ),
    "rings": ( 2, 4 ),
    "count": ( 2, 4 ),
  },
  {
    "range": ( 2/3, 1 ),
    "rings": ( 1, 3 ),
    "count": ( 3, 6 ),
  },
]

BUFFER = ( 1/100, 1/5 )

img_length = min( WIDTH, HEIGHT )

image = Image.new( 'RGB', ( WIDTH, HEIGHT ), NEUTRALS['white'] )
draw = ImageDraw.Draw( image )

ring_list = []

for ring_type in RING_TYPES:
  type_count = random.randrange( ring_type["count"][0], ring_type["count"][1] )
  angle_range = 2 * math.pi / type_count
  for count_num in range( type_count ):
    # center of rings
    angle = angle_range * ( random.random() + count_num )
    min_dist = img_length / 2 * ring_type["range"][0]
    max_dist = img_length / 2 * ring_type["range"][1]
    distance = ( max_dist - min_dist ) * random.random() + min_dist
    # x = r cos(theta)
    # y = r sin(theta)
    center_x = distance * math.cos( angle ) + WIDTH / 2
    center_y = distance * math.sin( angle ) + HEIGHT / 2

    radius = 0
    num_rings = random.randrange( ring_type["rings"][0], ring_type["rings"][1] )
    for ring_num in range( num_rings ):
      radius += random.randrange( img_length * BUFFER[0], img_length * BUFFER[1] + 1 )

      draw.ellipse(
        (
          center_x - radius,
          center_y - radius,
          center_x + radius,
          center_y + radius,
        ),
        outline = NEUTRALS['black'],
      )

      ring_list.append( {
        "center_x": center_x,
        "center_y": center_y,
        "radius": radius,
      } )

def is_in_ring( x, y, ring_dict ):
  # (x-h)^2 + (y-k)^2 < r^2
  return ( ( x - ring_dict["center_x"] ) ** 2 + ( y - ring_dict["center_y"] ) ** 2 ) < ring_dict["radius"] ** 2

section_colors = {}

pixels = image.load()
for w in range( WIDTH ):
  for h in range( HEIGHT ):
    pixel_section = ""
    for ring in ring_list:
      pixel_section += '1' if is_in_ring( w, h, ring ) else '0'
    if not pixel_section in section_colors:
      section_colors[ pixel_section ] = random_palette_color()
    pixels[ w, h ] = section_colors[ pixel_section ]

image.save( f"{ FILENAME }.png", "PNG" )
image.show()

