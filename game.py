from PPlay.window import *
from classes.table import Table

janela = Window(1920, 1040)
janela.set_title('Xadrez')
close = False
table = Table((300, 300))
print (">> inicio do jogo <<")
turn = "Brancas"

while not close:
  print ("*** Vez das", turn, "***")
  print ("TABULEIRO ATUAL: ")
  table.print_table()

  piece = None
  while not piece:
    piece_entry = input("Escolha as coordenadas de uma peça (x, y): ").split(" ")
    piece = table.findPiece((int(piece_entry[0]), int(piece_entry[1])))
    if piece == None:
      print("Peça não encontrada")

  possibilities = piece.availablePositions(table)
  print("Essas são as posições de movimento possiveis para essa peça: ", possibilities['move'])
  print("Essas são as posições de ataque possiveis para essa peça: ", possibilities['atack'])
  try:
    position_entry = input('Insira a coordenada para se movimentar: ').split(" ")
    piece.move((int(position_entry[0]), int(position_entry[1])), table)
    turn = "Brancas" if turn != "Brancas" else "Pretas"
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
