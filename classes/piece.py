import pdb
from PPlay.sprite import Sprite

class Piece(Sprite):
  def __init__(self, image_file, color, historic_positions):
    super().__init__(image_file)
    self.color = color
    self.historic_positions = historic_positions
    self.name = self.image_file.split("/")[2].split(".")[0]

  # Função que deve ser usada para realizar a movimentação da peça para uma posição no tabuleiro
  # Recebe uma tupla (x, y), o table, e uma flag de ignore_check.

  # Se a posição escolhida for valida, ele busca o conjunto de possibilidades de movimento da peça escolhida filtrada pela configuração atual do tabuleiro.
  # No caso ignore_check seja True, ele vai pegar as possibilidades gerais da peça, sem considerar a configuração do tabuleiro.
  # Por isso, a flag ignore_check deve ser sempre False para interações humanas, e True somente em casos de teste da maquina, como na própria função Table#filterAvailablePositions

  # Por fim, ele verifica se a posição escolhida está no conjunto e adiciona o movimento no historico, removendo a peça atacada do tabuleiro, caso necessário.
  def move(self, position_entry, table, ignore_check=False):
    if Piece.validPosition(position_entry):
      positions = table.filterAvailablePositions(self) if not ignore_check else self.availablePositions(table)

      for position in positions:
        if position[0] == position_entry:
          if (position[1] != None):
            table.pieces.remove(position[1])

          playerColor = 0 if self.color == 'white' else 1
          table.players[playerColor].historic_played_pieces.append(self)
          self.historic_positions.append(position)
          return

    raise Exception

  # Função que retorna o par (x, y) atual do historico de posições de uma peça.
  def actualPosition(self):
    return self.historic_positions[-1][0]

  # Função que desfaz o movimento dessa peça, e caso necessário, recoloca uma peça tomada durante o movimento.
  def undo(self, table):
    if self.historic_positions[-1][1] != None:
      table.pieces.append(self.historic_positions[-1][1])

    playerColor = 0 if self.color == 'white' else 1
    table.players[playerColor].historic_played_pieces.remove(self)

    self.historic_positions.remove(self.historic_positions[-1])
    if self.historic_positions[-1][2] == "promotion":
      self.unpromote(table)


  def unpromote(self, table):
    table.replacePiece(-1, self)

  # Função de classe que verifica se uma posição é valida dentro de um tabuleiro.
  def validPosition(new_position):
    return 0 <= new_position[0] <= 7 and 0 <= new_position[1] <= 7

