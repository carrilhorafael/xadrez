from PPlay.window import *
from classes.player import Player
from classes.table import Table
from utils.endGame import endGame

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
  if len(players[turn].possibleMoviments(table)) == 0:
    endGame(0)
    break

  print("Vez de", players[turn].name)

  print ("TABULEIRO ATUAL: ")
  table.print_table()

  piece = players[turn].choosePiece(table)
  possibilities = piece.availablePositions(table)
  print("Essas são as posições de movimento possiveis para essa peça: ", possibilities)
  try:
    players[turn].makeMove(piece, table)
    turn = not turn
  except Exception:
    print('jogada invalida, repita')
