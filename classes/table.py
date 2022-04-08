from PPlay.gameimage import GameImage
from classes.position import Position

class Table:
  def __init__(self, self_position, size):
    self.positions = self.createPositions()
    self.self_position = self_position + (self_position[0] + size, self_position[1] + size)
    self.size = size

  def createPositions(self):
    positions = []
    for i in range(0, 8, 1):
      line = []
      for j in range(0, 8, 1):
        color = 'black' if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0) else 'white'
        line.append(Position(color, (i, j)))
      positions.append(line)
    return positions

  def printTable(self):
    for i in range(0, 8, 1):
      for j in range(0, 8, 1):
        position = self.positions[i][j]
        position.set_position(i*64, j*64)
        position.draw()

