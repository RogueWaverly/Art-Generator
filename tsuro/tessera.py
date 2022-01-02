import random


class Tessera:
  pass


class Square(Tessera):

  def __init__( self,
      length,
      center_x,
      center_y,
      num_points = 2 ):

    self.length = length
    self.center_x = center_x
    self.center_y = center_y
    self.num_points = num_points
    self._outline = []

    self.buffer = self.length // ( self.num_points + 1 )

    self.init_points( )
    self.init_paths( )

  def init_points( self ):
    self.points = [ ]

    horizontal_x = [
      self.center_x - self.buffer // 2,
      self.center_x + self.buffer // 2,
    ]
    horizontal_y = [
      self.center_y - self.length // 2,
      self.center_y + self.length // 2,
    ]
    for h_x in horizontal_x:
      for h_y in horizontal_y:
        self.points.append( ( h_x, h_y ) )

    vertical_x = [
      self.center_x + self.length // 2,
      self.center_x - self.length // 2,
    ]
    vertical_y = [
      self.center_y - self.buffer // 2,
      self.center_y + self.buffer // 2,
    ]
    for v_x in vertical_x:
      for v_y in vertical_y:
        self.points.append( ( v_x, v_y ) )

  def init_paths( self ):
    self.paths = [ ]

    points = self.points
    random.shuffle( points )
    for point_idx in range( 0, len( points ), 2 ):
      self.paths.append( ( points[ point_idx ], points[ point_idx + 1 ] ) )

  def _init_outline( self ):
    self._outline = []
    self._outline.extend( [
      ( self.center_x - self.length // 2, self.center_y - self.length // 2 ),
      ( self.center_x + self.length // 2, self.center_y - self.length // 2 ),
      ( self.center_x + self.length // 2, self.center_y + self.length // 2 ),
      ( self.center_x - self.length // 2, self.center_y + self.length // 2 ),
    ] )

  def get_outline( self ):
    if not self._outline:
      self._init_outline()
    return self._outline

  def __str__( self ):

    tessera_str = f"""
Square:
\tlength: { self.length }
\tcenter_x: { self.center_x }
\tcenter_y: { self.center_y }
\tnum_points: { self.num_points }
\tbuffer: { self.buffer }
\tpaths:"""

    for path in self.paths:
      tessera_str += f"\n\t\t( { path[0][0] }, { path[0][1] } ) - ( { path[1][0] }, { path[1][1] } )"
    
    tessera_str += "\n\tlines:"
    for line in self.get_outline():
      tessera_str += f"\n\t\t( { line[0] }, { line[1] } )"

    return tessera_str
