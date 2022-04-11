from PPlay.sprite import Sprite

class Piece(Sprite):
  def __init__(self, image_file, color, initial_position):
    super().__init__(image_file)
    self.color = color
    self.historic_positions = [initial_position]

  def move(self, new_position, table):
    if (Piece.validPosition(new_position) and (new_position in self.availableMovePositions(table))):
      self.historic_positions.append(new_position)
    else:
      raise Exception('jogada invalida')

  def actualPosition(self):
    return self.historic_positions[-1]

  def availableMovePositions():
    raise Exception("Não implementada")

  def availableAtackPositions():
    raise Exception("Não implementada")

  def validPosition(new_position):
    return 0 <= new_position[0] <= 7 and 0 <= new_position[1] <= 7

