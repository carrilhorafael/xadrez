from classes.piece import Piece

class King(Piece):
  def __init__(self, color, position):
    image_file = './assets/' + color + 'King.png'
    super().__init__(image_file, position)

  def available_move_positions(self):
    positions = []
    for sum_y in (-1, 0, 1):
      for sum_x in (-1, 0, 1):
        new_position_x = self.position[0] + sum_x
        new_position_y = self.position[1] + sum_y
        new_position = (new_position_x, new_position_y)
        if new_position != self.position and Piece.valid_position(new_position):
          positions.append(new_position)

    return positions

