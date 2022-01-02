from PIL import Image, ImageDraw
from random import randrange

from mosaic import Grid

FILENAME = "test-tsuro"


WIDTH = 600
HEIGHT = 600
BLACK = (0,0,0)
WHITE = (256, 256, 256)

NUM_X = 10
NUM_Y = 10
SQ_LENGTH = 60
CENTER_X = WIDTH//2
CENTER_Y = HEIGHT//2

bg_color = ( randrange(256), randrange(256), randrange(256) )
outline_color = ( randrange(256), randrange(256), randrange(256) )
path_color = ( randrange(256), randrange(256), randrange(256) )

image = Image.new('RGB', (WIDTH, HEIGHT), bg_color )
draw = ImageDraw.Draw(image)


def draw_outline( mosaic ):
  for tessera in mosaic.tesserae:
    draw.polygon( tessera.get_outline(), outline=outline_color )

def draw_straight_paths( mosaic ):
  for tessera in mosaic.tesserae:
    for path in tessera.paths:
      draw.line( path, fill=path_color, width=2 )

def draw_bezier_paths( mosaic ):
  from bezier import make_bezier
  ts = [t/100.0 for t in range(101)]
  for tessera in mosaic.tesserae:
    for path in tessera.paths:
      bezier = make_bezier( [
        path[0],
        ( tessera.center_x, tessera.center_y ),
        path[1],
      ] )
      draw.line( bezier(ts), fill=path_color, width=2 )

grid = Grid( NUM_X, NUM_Y, SQ_LENGTH, CENTER_X, CENTER_Y )

draw_outline( grid )
draw_bezier_paths( grid )

image.save(FILENAME + ".png", "PNG")
image.show()
