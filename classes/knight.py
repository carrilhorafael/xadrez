from classes.piece import Piece


class Knight(Piece):
  def __init__(self, color, initial_position):
    self.image_file = './assets/' + color + 'Knight.png'
    self.points = 5
    super().__init__(self.image_file, color, initial_position)

  # Retorna um array de posição onde o primeiro indice é uma posição valida para se movimentar e o segundo indice uma peça inimiga que pode ser atacada.
  # Usar sempre a função table#filterAvailablePositions para garantir que as possibilidades sejam filtradas pela configuração atual do tabuleiro.
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
