from classes.piece import Piece

class King(Piece):
  def __init__(self, color, position):
    self.image_file = './assets/' + color + 'King.png'
    super().__init__(self.image_file, color, position)

  def availableMovePositions(self, table):
    positions = []
    for sum_y in (-1, 0, 1):
      for sum_x in (-1, 0, 1):
        if sum_x == 0 and sum_y == 0:
          continue
        new_position_x = self.actualPosition()[0] + sum_x
        new_position_y = self.actualPosition()[1] + sum_y
        new_position = (new_position_x, new_position_y)

        if Piece.validPosition(new_position) and table.findPiece(new_position) == None:
          positions.append(new_position)

    return positions

