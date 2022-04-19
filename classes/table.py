from classes.bishop import Bishop
from classes.king import King
from classes.knight import Knight
from classes.pawn import Pawn
from classes.position import Position
from classes.queen import Queen
from classes.rook import Rook
from PPlay.gameimage import *
from PPlay.mouse import *

initial_configuration = [
	['black_rook', 'black_knight', 'black_bishop', 'black_queen', 'black_king', 'black_bishop', 'black_knight',
	 'black_rook'],
	['black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn'],
	[],
	[],
	[],
	[],
	['white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn'],
	['white_rook', 'white_knight', 'white_bishop', 'white_queen', 'white_king', 'white_bishop', 'white_knight',
	 'white_rook']
]


class Table:
	def __init__(self, position, length):
		# Adicionei algumas variáveis para acesso a info mais fácil - discutir em grupo
		self.x = position[0]
		self.y = position[1]

		self.positions = None

		self.borderSize = 10
		self.border = None
		self.setBorder()

		self.setInitialPositions()
		self.setInitialPieces()


	def printTable(self):
		print(
			'----------------------------------------------------------------------------------------------------------'
			'---------')
		print('  | {:11s} | {:11s} | {:11s} | {:11s} | {:11s} | {:11s} | {:11s} | {:11s} |'.format('0', '1', '2', '3',
		                                                                                           '4', '5', '6', '7'))
		for line in self.positions:
			print(self.positions.index(line), end='')
			for position in line:
				print(" | ", end='')
				# color = 'b' if position.color == 'black' else 'w'

				empty_position = True
				# for piece in self.pieces:
				for i in range(0, 8, 1):
					for j in range(0, 8, 1):
						if self.positions[j][i].piece:
							if self.positions[j][i].piece.actualPosition() == position.position:
								empty_position = False
								print('{:11s}'.format(self.positions[j][i].piece.image_file.split("/")[2].split(".")[0]), end='')
								break

				if empty_position:
					print('{:11s}'.format("-"), end='')

			print(" |")
		print(
			'-----------------------------------------------------------------------------------------------------------'
			'--------')


	def setInitialPositions(self):
		positions = []
		for i in range(0, 8, 1):
			line = []
			for j in range(0, 8, 1):
				#color = 'black' if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0) else 'white'
				if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
					color = 'black'
				else:
					color = 'white'

				line.append(Position(color, (j, i)))
			positions.append(line)

		self.positions = positions
		self.setSquaresPosition()


	# Alterado
	def setInitialPieces(self):
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
						self.positions[j][i].setPiece(Rook(color, initial_position))
					elif piece_subclass == 'knight':
						self.positions[j][i].setPiece(Knight(color, initial_position))
					elif piece_subclass == 'bishop':
						self.positions[j][i].setPiece(Bishop(color, initial_position))
					elif piece_subclass == 'queen':
						self.positions[j][i].setPiece(Queen(color, initial_position))
					elif piece_subclass == 'king':
						self.positions[j][i].setPiece(King(color, initial_position))
					elif piece_subclass == 'pawn':
						self.positions[j][i].setPiece(Pawn(color, initial_position))


	def findPiece(self, position):
		for i in range(0, 8, 1):
			for j in range(0, 8, 1):
				if self.positions[i][j].piece:
					if self.positions[i][j].piece.actualPosition() == position:
						return self.positions[i][j].piece


# Novas funções, verificar utilidades e/ou junção com funções já existentes depois

	def verifyEntry(self):
		l = [0, 0]
		mouse = Mouse()
		while not mouse.is_button_pressed(1):
			for i in range(0, 8, 1):
				for j in range(0, 8, 1):
					start = [self.positions[i][j].x, self.positions[i][j].y]
					end = [self.positions[i][j].x + self.positions[i][j].length, self.positions[i][j].y + self.positions[i][j].length]
					print(start)
					print(end)
					print(mouse.get_position())
					print('')
					if mouse.is_over_area(start, end):
						self.positions[i][j].border.draw()
						if mouse.is_button_pressed(1):
							return (i, j)


	def updatePieces(self, old, new):
		self.positions[new[0]][new[1]].setPiece(self.positions[old[0]][old[1]].piece)
		self.positions[old[0]][old[1]].piece = None


	def setSquaresPosition(self):
		for i in range(0, 8, 1):
			for j in range(0, 8, 1):
				x = i * self.positions[i][j].length + self.x + self.borderSize
				y = j * self.positions[i][j].length + self.y + self.borderSize

				self.positions[i][j].set_position(x, y)
				self.positions[i][j].setBorderPosition()
				self.positions[i][j].setCirclePosition()


	# Criar uma classe Border e verificar se a borda é do tabuleiro ou da casa?
	def setBorder(self):
		self.border = GameImage('assets/table/borda_tabuleiro.png')
		self.border.set_position(self.x, self.y)


	def drawTable(self):
		for i in range(0, 8, 1):
			for j in range(0, 8, 1):
				self.positions[i][j].draw()
				# self.positions[i][j].circle.draw()
				# self.positions[i][j].border.draw()

		self.border.draw()


	def drawCircles(self, possibilities):
		for possibilty in possibilities:
			i = possibilty[0]
			j = possibilty[1]
			self.positions[i][j].circle.draw()


	def drawPieces(self):
		for i in range(0, 8, 1):
			for j in range(0, 8, 1):
				if self.positions[i][j].piece:
					self.positions[i][j].piece.draw()

'''
REFATORAÇÕES
- Deixei o if else mais explícito para entendimento mais rápido do código. Já seria melhor deixar explícito normalmente, 
mas, nesse caso principalmente, é ainda melhor porque nem todos do nosso grupo estão habituados com a linguagem Python
- Botei espaços nas operçãoes de % para ficar mais legível e organizado
- Mudei de 1 para 2 a quantidade de linhas brancas entre os métodos da classe. Dessa forma, os métodos ficarem mais le-
gíveis e não confundír uns com os outros
- Adicionei linhas em branco nos métodos sempre que achei necessário dividir tarefas dentro dos mesmos
- Adicionei as propriedades no construtor para ficar mais claro quais são todas elas sem precisar analisar cada método
separadamente
'''