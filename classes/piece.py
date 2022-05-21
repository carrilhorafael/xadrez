import pdb
from PPlay.sprite import Sprite

class Piece(Sprite):
  def __init__(self, image_file, color, initial_position):
    super().__init__(image_file)
    self.color = color
    self.historic_positions = [(initial_position, None)]
    self.name = self.image_file.split("/")[2].split(".")[0]

  def move(self, position_entry, table, ignore_check=False):
    positions = table.filterAvailablePositions(self) if not ignore_check else self.availablePositions(table)

    for position in positions:
      if Piece.validPosition(position_entry) and position[0] == position_entry:
        if (position[1] != None):
          table.pieces.remove(position[1])
        self.historic_positions.append(position)
        return

  def actualPosition(self):
    return self.historic_positions[-1][0]

  def undo(self, table):
    if self.historic_positions[-1][1] != None:
      table.pieces.append(self.historic_positions[-1][1])
    self.historic_positions.remove(self.historic_positions[-1])

  def validPosition(new_position):
    return 0 <= new_position[0] <= 7 and 0 <= new_position[1] <= 7

