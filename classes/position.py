from PPlay.sprite import Sprite

class Position(Sprite):
  def __init__(self, color, position):
    image_file = './assets/' + color + 'Position.jpg'
    super().__init__(image_file)
    self.position = position
    self.color = color
