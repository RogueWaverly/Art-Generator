from tessera import Square


class Mosaic:
  pass


class Grid( Mosaic ):

  def __init__(
      self,
      num_x,
      num_y,
      length,
      center_x,
      center_y,
      num_points=2 ):

    self.num_x = num_x
    self.num_y = num_y
    self.length = length
    self.center_x = center_x
    self.center_y = center_y
    self.num_points = num_points

    self.init_tesserae( )

  def init_tesserae( self ):
    self.tesserae = []

    zero_x = self.center_x - ( self.length // 2 ) * ( self.num_x - 1 )
    zero_y = self.center_y - ( self.length // 2 ) * ( self.num_y - 1 )
    for n_x in range( self.num_x ):
      for n_y in range( self.num_y ):
        sq_x = zero_x + ( n_x * self.length )
        sq_y = zero_y + ( n_y * self.length )
        self.tesserae.append( Square( self.length, sq_x, sq_y, self.num_points ) )
