from PPlay.sprite import Sprite

class Position(Sprite):
	# Alterado
	def __init__(self, color, position):
		image_file = './assets/' + color + 'Position.jpg'
		super().__init__(image_file)
		self.position = position
		self.color = color

		# Adicionei um Sprite border para a casa em questão sempre ter uma borda própria e utilizar a mesma poisção da
		# casa
		self.border = Sprite('assets/table/borda_marrom.png')

		# Adicionei um Sprite circle para a casa em questão sempre ter um círculo próprio e utilizar a poisção central
		# da casa
		self.circle = Sprite('assets/table/circle.png')

		# Adicionei um Sprite circle para a casa em questão sempre ter um círculo próprio e utilizar a poisção central
		# da casa
		self.piece = None

		# Adicionei uma variável 'length' para não precisar usar width ou height(no caso dessa classe que é um quadrado)
		self.length = self.width


	# Criar uma classe Border e verificar se a borda é do tabuleiro ou da casa?
	def setBorderPosition(self):
		self.border.set_position(self.x, self.y)


	def setCirclePosition(self):
		x = self.x + (self.length - self.circle.width) / 2
		y = self.y + (self.length - self.circle.height) / 2

		self.circle.set_position(x, y)


	def setPiece(self, piece):
		self.piece = piece
		x = self.x + (self.length - self.piece.width) / 2
		y = self.y + (self.length - self.piece.height) / 2

		self.piece.set_position(x, y)


	def drawBorder(self):
		self.border.draw()