from PPlay.window import *
from classes.table import Table

janela = Window(1920, 1040)
janela.set_title('Xadrez')
close = False
table = Table((300, 300))
print (">> inicio do jogo <<")

while not close:
  print ("TABULEIRO ATUAL: ")
  table.print_table()

  piece_entry = input("Escolha as coordenadas de uma peça (x, y): ").split(" ")
  piece = table.findPiece((int(piece_entry[0]), int(piece_entry[1])))

  possibilities = piece.availableMovePositions(table)
  print("Essas são as posições possiveis para essa peça: ", possibilities)
  try:
    position_entry = input('Insira a coordenada para se movimentar: ').split(" ")
    piece.move((int(position_entry[0]), int(position_entry[1])), table)
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
