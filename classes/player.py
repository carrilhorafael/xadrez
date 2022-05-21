import pdb
from random import randint
import time
class Player:
  def __init__(self, system_controlled, color, name="IA"):
    self.system_controlled = system_controlled
    self.name = name
    self.color = color

  # Função que reune as rotinas de uma jogada, separadas por rotina da IA ou do jogador humano.

  # Se for um jogador humano:
      # Sistema pede uma posição do jogador até encontrar a peça do movimento.
      # Sistema exibe as possibilidades de movimento da peça
      # Sistema pede uma coordenada para movimentar
      # Sistema tenta executar o movimento.

  # Se for uma IA:
      # Executa a função calcBetterMovement que retorna um par (peça, posição) para movimentar.
      # Sistema tenta executar o movimento.
      # Sistema entra em delay de alguns ms.
  def makeMove(self, table):
    piece = None

    if not self.system_controlled:
      while not piece:
        piece_entry = tuple(map(int, input("Escolha as coordenadas de uma peça (x, y): ").split(" ")))
        piece = table.findPiece(piece_entry, self.color)
        if piece == None:
          print("Jogada inválida")

      table.print_table(pieceSelected=piece)
      position_entry = tuple(map(int, input('Insira a coordenada para se movimentar (x, y): ').split(" ")))
    else:
      better_movement = self.calcBetterMovement(table)
      piece = better_movement[0]
      position_entry = better_movement[1]

    piece.move(position_entry, table)
    if self.system_controlled:
      time.sleep(0.3)

  # Função que retorna o rei da cor do jogador (utilizado para facilitar as rotinas xeque e xeque-mate)
  def king(self, table):
    for piece in table.playerPieces(self.color):
      if (piece.name == self.color+'King'):
        return piece
    return None

  # Função que retorna todas as possiveis movimentações de um jogador seguindo um par de (peça, lista de possiveis movimentações dessa peça)
  def possibleMovements(self, table):
    return_possibilities = []
    for piece in table.playerPieces(self.color):
      piece_available_positions = table.filterAvailablePositions(piece)
      if len(piece_available_positions) > 0:
        return_possibilities.append((piece, piece_available_positions))
    return return_possibilities

  # Função que verifica se o rei do jogador está sob ataque de alguma peça inimiga
  def underCheck(self, table):
    enemyColor = 1 if self.color == 'white' else 0
    enemy = table.players[enemyColor]
    king = self.king(table)

    for piece in table.playerPieces(enemy.color):
      if len(list(filter(lambda x: x[1] == king, piece.availablePositions(table)))) > 0:
        return True
    return False

  # Função que retorna o melhor movimento para a IA (deve ser incrementado com a inteligencia deterministica de movimentação)
  def calcBetterMovement(self, table):
    moves = self.possibleMovements(table)
    atack_movements = []
    for possibilities in moves:
      for move in possibilities[1]:
        if move[1] != None:
          atack_movements.append((possibilities[0], move[0], move[1]))

    if len(atack_movements) > 0:
      atack_movements.sort(key=lambda move: move[2].points, reverse=True)
      return (atack_movements[0][0], atack_movements[0][1])
    else:
      moves.sort(key=lambda move: move[0].points)
      movement = moves[randint(0, len(moves)-1)]
      piece = movement[0]
      position_entry = movement[1][randint(0, len(movement[1])-1)][0]
      return (piece, position_entry)



