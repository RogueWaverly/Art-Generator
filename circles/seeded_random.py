import random
import sys


def seeded_random( seed=None ):
  if seed is None:
    seed = random.randrange( sys.maxsize )
  random.seed( seed )
  print( f"seed: { seed }" )
  return random
