from classes.piece import Piece

class King(Piece):
  def __init__(self, color, position):
    self.image_file = './assets/' + color + 'King.png'
    super().__init__(self.image_file, color, position)

  def availablePositions(self, table):
    move_positions = []
    atack_positions = []
    for sum_y in (-1, 0, 1):
      for sum_x in (-1, 0, 1):
        if sum_x == 0 and sum_y == 0:
          continue
        new_position_x = self.actualPosition()[0] + sum_x
        new_position_y = self.actualPosition()[1] + sum_y
        new_position = (new_position_x, new_position_y)
        other_piece = table.findPiece(new_position)

        if Piece.validPosition(new_position) and other_piece == None:
          move_positions.append(new_position)
        elif other_piece != None and other_piece.color != self.color:
          atack_positions.append(new_position)


    return { 'move': move_positions, 'atack': atack_positions }
