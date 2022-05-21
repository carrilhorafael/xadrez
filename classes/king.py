from classes.piece import Piece

class King(Piece):
  def __init__(self, color, position):
    self.image_file = './assets/' + color + 'King.png'
    self.points = 150
    super().__init__(self.image_file, color, position)

  # Retorna um array de posição onde o primeiro indice é uma posição valida para se movimentar e o segundo indice uma peça inimiga que pode ser atacada.
  # Usar sempre a função table#filterAvailablePositions para garantir que as possibilidades sejam filtradas pela configuração atual do tabuleiro.
  def availablePositions(self, table):
    return_possibilities = []
    for sum_y in (-1, 0, 1):
      for sum_x in (-1, 0, 1):
        if sum_x == 0 and sum_y == 0:
          continue
        new_position_x = self.actualPosition()[0] + sum_x
        new_position_y = self.actualPosition()[1] + sum_y
        new_position = (new_position_x, new_position_y)
        other_piece = table.findPiece(new_position)

        if Piece.validPosition(new_position) and other_piece == None:
          return_possibilities.append([new_position, other_piece])
        elif other_piece != None and other_piece.color != self.color:
          return_possibilities.append([new_position, other_piece])


    return return_possibilities
