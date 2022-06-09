import random
from classes.piece import Piece

class Pawn (Piece):
  def __init__(self, *args):
    self.points = 1
    if len(args) == 2:
      self.image_file = './assets/' + args[0] + 'Pawn.png'
      super().__init__(self.image_file, args[0], args[1])
    elif len(args) == 1:
      self.image_file = './assets/' + args[0].color + 'Pawn.png'
      super().__init__(self.image_file, args[0].color, args[0].historic_positions)


  def move(self, position_entry, table, ignore_check=False):
    if Piece.validPosition(position_entry):
      positions = table.filterAvailablePositions(self) if not ignore_check else self.availablePositions(table)

      for position in positions: #position é [(x, y), peca_atacada, movimento_especial]
        if position[0] == position_entry:
          if (position[1] != None):
            table.pieces.remove(position[1])
          self.historic_positions.append(position)

          if position[2] == "promotion":
            if ignore_check or table.playerOfColor(self.color).system_controlled:
              promote_piece = random.randint(0, 3)
            else:
              promote_piece = int(input('Escolha uma nova peça para promover:\n0 - Rainha, 1 - Torre, 2 - Cavalo, 3 - Bispo\n'))
              while promote_piece not in (0, 1, 2, 3):
                print('escolha invalida')
                promote_piece = int(input('Escolha uma nova peça para promover:\n0 - Rainha, 1 - Torre, 2 - Cavalo, 3 - Bispo\n'))

            new_piece = self.promote(table, promote_piece)
            table.playerOfColor(self.color).historic_played_pieces.append(new_piece)
            return new_piece

          table.playerOfColor(self.color).historic_played_pieces.append(self)
          return self
    raise Exception

  def promote(self, table, promote_piece):
    return table.replacePiece(promote_piece, self)

  # Retorna um array de posição onde o primeiro indice é uma posição valida para se movimentar e o segundo indice uma peça inimiga que pode ser atacada.
  # Usar sempre a função table#filterAvailablePositions para garantir que as possibilidades sejam filtradas pela configuração atual do tabuleiro.
  def availablePositions(self, table):
    return_possibilities = []

    if (self.color == 'black'):
      for i in (-1, 1):
        new_position = (self.actualPosition()[0] + i, self.actualPosition()[1] + 1)
        other_piece = table.findPiece(new_position)
        if other_piece != None and other_piece.color != self.color:
          if new_position[1] == 7:
            return_possibilities.append([new_position, other_piece, "promotion"])
          else:
            return_possibilities.append([new_position, other_piece, None])

      for i in (-1, 1):
        new_position = (self.actualPosition()[0] + i, self.actualPosition()[1] + 1)
        attack_position = (self.actualPosition()[0] + i, self.actualPosition()[1])
        other_piece = table.findPiece(attack_position)
        if other_piece != None and other_piece.name == 'whitePawn' and len(table.players[0].historic_played_pieces) > 0:
          last_played_piece = table.players[0].historic_played_pieces[-1]
          if last_played_piece == other_piece:
            return_possibilities.append([new_position, other_piece, "en_passant"])

      if (len(self.historic_positions) > 1):
        new_position = (self.actualPosition()[0], self.actualPosition()[1] + 1)
        other_piece = table.findPiece(new_position)
        if Piece.validPosition(new_position):
          if other_piece == None:
            if new_position[1] == 7:
              return_possibilities.append([new_position, other_piece, "promotion"])
            else:
              return_possibilities.append([new_position, other_piece, None])
      else:
        new_position = (self.actualPosition()[0], self.actualPosition()[1] + 1)
        other_piece = table.findPiece(new_position)
        if Piece.validPosition(new_position) and other_piece == None:
          if new_position[1] == 7:
            return_possibilities.append([new_position, other_piece, "promotion"])
          else:
            return_possibilities.append([new_position, other_piece, None])
          new_position = (self.actualPosition()[0], self.actualPosition()[1] + 2)
          other_piece = table.findPiece(new_position)
          if Piece.validPosition(new_position) and other_piece == None:
            if new_position[1] == 7:
              return_possibilities.append([new_position, other_piece, "promotion"])
            else:
              return_possibilities.append([new_position, other_piece, None])


    else:
      for i in (-1, 1):
        new_position = (self.actualPosition()[0] + i, self.actualPosition()[1] - 1)
        other_piece = table.findPiece(new_position)
        if other_piece != None and other_piece.color != self.color:
          if new_position[1] == 0:
            return_possibilities.append([new_position, other_piece, "promotion"])
          else:
            return_possibilities.append([new_position, other_piece, None])

      for i in (-1, 1):
        new_position = (self.actualPosition()[0] + i, self.actualPosition()[1] - 1)
        attack_position = (self.actualPosition()[0] + i, self.actualPosition()[1])
        other_piece = table.findPiece(attack_position)
        if other_piece!= None and other_piece.name == 'blackPawn' and len(table.players[1].historic_played_pieces) > 0:
          last_played_piece = table.players[1].historic_played_pieces[-1]
          if last_played_piece == other_piece:
            return_possibilities.append([new_position, other_piece, "en_passant"])

      if (len(self.historic_positions) > 1):
        new_position = (self.actualPosition()[0], self.actualPosition()[1] - 1)
        other_piece = table.findPiece(new_position)
        if Piece.validPosition(new_position) and other_piece == None:
          if new_position[1] == 0:
            return_possibilities.append([new_position, other_piece, "promotion"])
          else:
            return_possibilities.append([new_position, other_piece, None])
      else:
        new_position = (self.actualPosition()[0], self.actualPosition()[1] - 1)
        other_piece = table.findPiece(new_position)
        if Piece.validPosition(new_position) and other_piece == None:
          if new_position[1] == 0:
            return_possibilities.append([new_position, other_piece, "promotion"])
          else:
            return_possibilities.append([new_position, other_piece, None])
          new_position = (self.actualPosition()[0], self.actualPosition()[1] - 2)
          other_piece = table.findPiece(new_position)
          if Piece.validPosition(new_position) and other_piece == None:
            if new_position[1] == 0:
              return_possibilities.append([new_position, other_piece, "promotion"])
            else:
              return_possibilities.append([new_position, other_piece, None])

    return return_possibilities
