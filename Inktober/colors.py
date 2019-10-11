colors = {
  'black': (0, 0, 0),
  'lime': (153, 255, 153),
  'periwinkle': (153, 153, 255),
  'cyan': (153, 255, 255),
  'red': (255, 153, 153),
  'canary': (255, 255, 153),
  'magenta': (255, 153, 255),
  'white': (255, 255, 255),
  'taiwan-blue': (0, 0, 151),
  'taiwan-red': (254, 0, 0),
}

def random_color():
  import random
  return random.choice(list(colors.values()))
