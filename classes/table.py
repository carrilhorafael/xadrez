from classes.bishop import Bishop
from classes.king import King
from classes.knight import Knight
from classes.pawn import Pawn
from classes.position import Position
from classes.queen import Queen
from classes.rook import Rook
from utils.prettyOutput import *

default_configuration = [
  ['black_rook', 'black_knight', 'black_bishop', 'black_queen', 'black_king', 'black_bishop', 'black_knight', 'black_rook'],
  ['black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn'],
  [],
  [],
  [],
  [],
  ['white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn'],
  ['white_rook', 'white_knight', 'white_bishop', 'white_queen', 'white_king', 'white_bishop', 'white_knight', 'white_rook']
]

class Table:
  def __init__(self, self_position, initial_configuration=default_configuration):
    self.setInitialPositions()
    self.setInitialPieces(initial_configuration)
    self.self_position = self_position

  def print_table(self, pieceSelected=None):
    print('-------------------------------------------------------------------------------------------------------------------')
    with prettyOutput(FG_CYAN) as out:
      out.write('  | {:11s} | {:11s} | {:11s} | {:11s} | {:11s} | {:11s} | {:11s} | {:11s} |'.format('0', '1', '2', '3',
                                                                                                     '4', '5', '6', '7'))
    for line in self.positions:
      print(self.positions.index(line), end='')
      for position in line:
        print(" | ", end='')

        empty_position = True
        for piece in self.pieces:
          if piece.actualPosition() == position.position:
            empty_position = False

            if pieceSelected != None and piece.actualPosition() in list(map(lambda p: p[0], pieceSelected.availablePositions(self))):
              with prettyOutput(FG_RED) as out:
                out.write('{:11s}'.format(piece.name), end='')
              break

            if piece == pieceSelected:
              with prettyOutput(FG_GREEN) as out:
                out.write('{:11s}'.format(piece.name), end='')
              break

            piece_color = FG_BLUE if piece.color == 'black' else FG_CYAN
            with prettyOutput(piece_color) as out:
              out.write('{:11s}'.format(piece.name), end='')
            break

        if empty_position:
          if pieceSelected != None and position.position in list(map(lambda p: p[0], pieceSelected.availablePositions(self))):
            with prettyOutput(FG_GREEN) as out:
              out.write('     *     ', end='')
          else:
            with prettyOutput(FG_WHITE) as out:
              out.write('     -     ', end='')

      print (" |")
    print('-------------------------------------------------------------------------------------------------------------------')

  def setInitialPositions(self):
    positions = []
    for i in range(0, 8, 1):
      line = []
      for j in range(0, 8, 1):
        color = 'black' if (i%2 == 0 and j%2 != 0) or (i%2 != 0 and j%2 == 0) else 'white'
        line.append(Position(color, (j, i)))
      positions.append(line)

    self.positions = positions

  def setInitialPieces(self, initial_configuration):
    pieces = []
    for i in range(0, 8, 1):
      list = initial_configuration[i]
      for j in range(0, len(list), 1):
        item = list[j]
        if(item != None):
          splitted_str = item.split('_')
          color = splitted_str[0]
          piece_subclass = splitted_str[1]
          initial_position = (j, i)

          if piece_subclass == 'rook':
            pieces.append(Rook(color, initial_position))
          elif piece_subclass == 'knight':
            pieces.append(Knight(color, initial_position))
          elif piece_subclass == 'bishop':
            pieces.append(Bishop(color, initial_position))
          elif piece_subclass == 'queen':
            pieces.append(Queen(color, initial_position))
          elif piece_subclass == 'king':
            pieces.append(King(color, initial_position))
          elif piece_subclass == 'pawn':
            pieces.append(Pawn(color, initial_position))
    self.pieces = pieces

  def findPiece(self, position, color='both'):
    if (color == 'both'):
      for piece in self.pieces:
        if piece.actualPosition() == position:
          return piece
    else:
      for piece in list(filter(lambda piece: piece.color == color, self.pieces)):
        if piece.actualPosition() == position:
          return piece

  def playerPieces(self, playerColor):
    return list(filter(lambda piece: piece.color == playerColor, self.pieces))

  def kingExists(self, playerColor):
    for piece in self.playerPieces(playerColor):
      if (piece.name == playerColor+'King'):
        return True
    return False
