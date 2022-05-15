from PPlay.sprite import Sprite

class Piece(Sprite):
  def __init__(self, image_file, color, initial_position):
    super().__init__(image_file)
    self.color = color
    self.historic_positions = [initial_position]
    self.name = self.image_file.split("/")[2].split(".")[0]

  def move(self, position_entry, table):
    positions = self.availablePositions(table)
    if Piece.validPosition(position_entry):
      position_index = list(map(lambda movement: movement[0], positions)).index(position_entry)
      new_position = positions[position_index]
      if (new_position[1] != None):
        table.pieces.remove(new_position[1])
      self.historic_positions.append(new_position[0])
    else:
      raise Exception('jogada invalida')

  def actualPosition(self):
    return self.historic_positions[-1]

  def validPosition(new_position):
    return 0 <= new_position[0] <= 7 and 0 <= new_position[1] <= 7

