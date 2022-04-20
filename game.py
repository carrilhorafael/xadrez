from PPlay.window import *
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.keyboard import *
from classes.table import Table

janela = Window(0, 0)
fundo = GameImage('assets/fundo_madeira.jpg')
borda = GameImage('assets/table/woodenBorderTable.png')

windowWidth = fundo.width
windowHeight = fundo.height
tableLength = borda.width

# janela = Window(1920, 1040)
janela = Window(windowWidth, windowHeight)
janela.set_title('Xadrez')
janela.set_background_color([0, 0, 0])

windowMidHeight = (windowHeight - tableLength) / 2
table = Table([windowMidHeight, windowMidHeight], tableLength)

# mouse = janela.get_mouse()
# keyboard = janela.get_keyboard()

close = False

cont = 0
while not close:
	cont += 1
	# table.printTable()

	table.drawTable()
	table.drawPieces()

	# piece_entry = tuple(map(int, input("Escolha as coordenadas de uma peça (x, y): ").split(" ")))
	piece_entry = table.verifyEntry(janela, None)
	piece = table.findPiece(piece_entry)
	print(cont)

	possibilities = piece.availableMovePositions(table)

	print("Essas são as posições possiveis para essa peça: ", possibilities)
	# try:
	position_entry = table.verifyEntry(janela, possibilities)
	table.updatePieces(piece_entry, position_entry)

		# piece.move(position_entry, table)
	# except Exception:
	# 	print('jogada invalida, repita')

	janela.update()

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

'''
REFATORAÇÕES
- Tamanho da janela menor para caber na minha tela
- Como acrescentei um parâmetro à classe Table, acrescentei, também, a informação de tamanho no instanciamento da mesma 
'''