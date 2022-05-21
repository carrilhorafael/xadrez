import pdb
from PPlay.window import *
from classes.player import Player
from classes.table import Table
from utils.endGame import endGame
from utils.prettyOutput import *
import time

mocked_configuration = [
  ['black_rook', 'black_knight', 'black_bishop', 'black_queen', 'black_king', 'black_bishop', 'black_knight', 'black_rook'],
  ['black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn'],
  [],
  [],
  [],
  [],
  ['white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn'],
  ['white_rook', 'white_knight', 'white_bishop', 'white_queen', 'white_king', 'white_bishop', 'white_knight', 'white_rook']
]


players = [Player(True, 'white', "IA 1"), Player(True, 'black', 'IA 2')]
players.sort(reverse=True, key=lambda player: player.color == 'white')

janela = Window(1920, 1040)
janela.set_title('Xadrez')
table = Table((300, 300), players, initial_configuration=mocked_configuration)
turn = 0

while True:
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

  table.printTable()
  try:
    players[turn].makeMove(table)

    if players[not turn].king(table) == None:
      endGame(1, winner=players[turn])
      break

    turn = not turn
  except Exception:
    print('jogada invalida, repita')
