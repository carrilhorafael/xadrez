from classes.piece import Piece


class Knight(Piece):
  def __init__(self, color, initial_position):
    self.image_file = './assets/' + color + 'Knight.png'
    super().__init__(self.image_file, color, initial_position)

  def availablePositions(self, table):
    return_possibilities = []

    for sum_y in (-2, 2):
      for sum_x in (-1, 1):
        new_position = (self.actualPosition()[0] + sum_x, self.actualPosition()[1] + sum_y)
        other_piece = table.findPiece(new_position)
        if Piece.validPosition(new_position):
          if other_piece == None:
            return_possibilities.append([new_position, other_piece])
          elif other_piece.color != self.color:
            return_possibilities.append([new_position, other_piece])

    for sum_x in (-2, 2):
      for sum_y in (-1, 1):
        new_position = (self.actualPosition()[0] + sum_x, self.actualPosition()[1] + sum_y)
        other_piece = table.findPiece(new_position)
        if Piece.validPosition(new_position):
          if other_piece == None:
            return_possibilities.append([new_position, other_piece])
          elif other_piece.color != self.color:
            return_possibilities.append([new_position, other_piece])

    return return_possibilities
