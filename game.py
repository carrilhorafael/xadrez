from PPlay.window import *
from classes.player import Player
from classes.table import Table

janela = Window(1920, 1040)
janela.set_title('Xadrez')
close = False
table = Table((300, 300))

player_name = input("Digite seu nome de usuário: ")
player_color = int(input ('Selecione a cor que pretende jogar: \n 0 - brancas | 1 - pretas\n' ))
while player_color not in [0, 1]:
  print('escolha invalida')
  player_color = int(input ('Selecione a cor que pretende jogar: \n 0 - brancas | 1 - pretas'))

player1_color = 'black' if player_color else 'white'
player2_color = 'white' if player_color else 'black'

players = [Player(False, player1_color, player_name), Player(True, player2_color)]
players.sort(reverse=True, key=lambda player: player.color == 'white')
turn = 0

while not close:
  print("vez de ", players[turn].name)

  print ("TABULEIRO ATUAL: ")
  table.print_table()

  piece = players[turn].choosePiece(table)
  possibilities = piece.availablePositions(table)
  print("Essas são as posições de movimento possiveis para essa peça: ", possibilities['move'])
  print("Essas são as posições de ataque possiveis para essa peça: ", possibilities['atack'])
  try:
    position_entry = input('Insira a coordenada para se movimentar: ').split(" ")
    piece.move((int(position_entry[0]), int(position_entry[1])), table)
    turn = not turn
  except Exception:
    print('jogada invalida, repita')

# while not close:


# table = Table((100, 50))
# king = King('black', (4, 0))

# print("posição inicial: " + str(king.position))
# while not close:
#   table.print_table()


#   print("posição atual: " + str(king.position))

#   print("posições possiveis: ", possibilities)
#   try:
#     entry = input('Insira a posição para se movimentar: ')
#     king.move(possibilities[int(entry)])
#   except Exception:
#     print('jogada invalida, repita')

# king.move((3, 0))
# print("posição atual: " + str(king.position))
# king.move((4, 0))
# print("posição atual: " + str(king.position))

# while not close:
#   janela.set_background_color((255,0,0))
#   table.print_table()
#   janela.update()
