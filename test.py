from PPlay.window import *
from classes.player import Player
from classes.table import Table
from utils.endGame import endGame
from utils.prettyOutput import *
import time

mocked_configuration = [
  ['black_rook', 'black_knight', 'black_bishop', 'black_queen', 'black_king', 'black_bishop', 'black_knight', 'black_rook'],
  ['black_pawn', 'black_pawn', 'black_pawn', None, 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn'],
  [],
  [None, None, None, 'black_pawn'],
  [None, None, 'white_pawn'],
  [],
  ['white_pawn', 'white_pawn', None, 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn'],
  ['white_rook', 'white_knight', 'white_bishop', 'white_queen', 'white_king', 'white_bishop', 'white_knight', 'white_rook']
]

janela = Window(1920, 1040)
janela.set_title('Xadrez')
table = Table((300, 300), initial_configuration=mocked_configuration)

players = [Player(True, 'white', "IA 1"), Player(True, 'black', 'IA 2')]
players.sort(reverse=True, key=lambda player: player.color == 'white')
turn = 0

while True:
  # Check for tie end game
  if not table.kingExists(players[turn].color):
    endGame(1, winner=players[not turn])
    break

  if len(players[turn].possibleMovements(table)) == 0:
    endGame(0)
    break

  with prettyOutput(FG_GREEN) as out:
    out.write('*******************************************************************************************************************')

  if not players[turn].system_controlled:
    with prettyOutput(FG_GREEN) as out:
      out.write('Vez de ' + players[turn].name)
  else:
    with prettyOutput(FG_MAGENTA) as out:
      out.write('Jogada de ' + players[turn].name)

  table.print_table()
  piece = players[turn].choosePiece(table)
  table.print_table(pieceSelected=piece)

  try:
    players[turn].makeMove(piece, table)
    turn = not turn

  except Exception:
    print('jogada invalida, repita')
