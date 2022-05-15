from random import randint
import time
class Player:
  def __init__(self, system_controlled, color, name="IA"):
    self.system_controlled = system_controlled
    self.name = name
    self.color = color

  def choosePiece(self, table):
    piece = None
    if not self.system_controlled:
      while not piece:
        piece_entry = tuple(map(int, input("Escolha as coordenadas de uma peça (x, y): ").split(" ")))
        piece = table.findPiece(piece_entry, self.color)
        if piece == None:
          print("Jogada inválida")
    else:
      piece_index = randint(0, len(self.possibleMovements(table)) - 1)
      piece = self.possibleMovements(table)[piece_index][0]

    if self.system_controlled:
      time.sleep(0.5)
    return piece

  def makeMove(self, piece, table):
    if not self.system_controlled:
      position_entry = tuple(map(int, input('Insira a coordenada para se movimentar (x, y): ').split(" ")))
    else:
      available_positions = piece.availablePositions(table)
      position_index = randint(0, len(available_positions) - 1)
      position_entry = available_positions[position_index][0]

    piece.move(position_entry, table)
    if self.system_controlled:
      time.sleep(0.5)

  def possibleMovements(self, table):
    return_possibilities = []
    for piece in table.playerPieces(self.color):
      piece_available_positions = piece.availablePositions(table)
      if len(piece_available_positions) > 0:
        return_possibilities.append((piece, piece_available_positions))
    return return_possibilities
