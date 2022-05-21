from PPlay.window import *
from classes.player import Player
from classes.table import Table
from utils.endGame import endGame
from utils.prettyOutput import *
import time

janela = Window(1920, 1040)
janela.set_title('Xadrez')
table = Table((300, 300))

player_name = input("Digite seu nome de usuário: ")
player_color = int(input ('Selecione a cor que pretende jogar: \n0 - brancas | 1 - pretas\n' ))
while player_color not in [0, 1]:
  print('escolha invalida')
  player_color = int(input ('Selecione a cor que pretende jogar: \n0 - brancas | 1 - pretas'))

player1_color = 'black' if player_color else 'white'
player2_color = 'white' if player_color else 'black'

players = [Player(False, player1_color, player_name), Player(True, player2_color)]
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

  table.printTable()
  piece = players[turn].choosePiece(table)
  table.printTable(pieceSelected=piece)

  try:
    players[turn].makeMove(piece, table)
    turn = not turn
  except Exception:
    print('jogada invalida, repita')
