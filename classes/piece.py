from PPlay.sprite import Sprite

class Piece(Sprite):
  def __init__(self, image_file, initial_position):
    super().__init__(image_file)
    self.position = initial_position

  def move(self, new_position):
    if (Piece.valid_position(new_position) and (new_position in self.available_move_positions())):
      self.position = new_position
      # atualizar a peça no tabuleiro
    else:
      raise Exception('jogada invalida')

  def available_move_positions():
    raise Exception("Não implementada")

  def available_atack_positions():
    raise Exception("Não implementada")

  def valid_position(new_position):
    return 0 <= new_position[0] <= 7 and 0 <= new_position[1] <= 7

