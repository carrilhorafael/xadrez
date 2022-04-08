from PPlay.gameobject import GameObject
from PPlay.sprite import Sprite

class Position(Sprite):
  def __init__(self, color, self_position):
    super().__init__('./assets/' + color + '.png')
    self.color = color
    self.self_position = self_position
