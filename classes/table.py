from classes.bishop import Bishop
from classes.king import King
from classes.knight import Knight
from classes.pawn import Pawn
from classes.position import Position
from classes.queen import Queen
from classes.rook import Rook

initial_configuration = [
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
  def __init__(self, self_position):
    self.setInitialPositions()
    self.setInitialPieces()
    self.self_position = self_position

  def print_table(self):
    print('-------------------------------------------------------------------------------------------------------------------')
    print ('  | {:11s} | {:11s} | {:11s} | {:11s} | {:11s} | {:11s} | {:11s} | {:11s} |'.format('0', '1', '2', '3', '4', '5', '6', '7'))
    for line in self.positions:
      print(self.positions.index(line), end='')
      for position in line:
        print(" | ", end='')

        empty_position = True
        for piece in self.pieces:
          if piece.actualPosition() == position.position:
            empty_position = False
            print('{:11s}'.format(piece.image_file.split("/")[2].split(".")[0]), end='')
            break

        if empty_position:
          print('{:11s}'.format("-"), end='')

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

  def setInitialPieces(self):
    pieces = []
    for i in range(0, 8, 1):
      list = initial_configuration[i]
      if len(list) > 0:
        for j in range(0, 8, 1):
          item = list[j]
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

  def findPiece(self, position):
    for piece in self.pieces:
      if piece.actualPosition() == position:
        print(piece)
        return piece
