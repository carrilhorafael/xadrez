from classes.piece import Piece

class Knight(Piece):
	def __init__(self, color, initial_position):
		self.image_file = './assets/' + color + 'Knight.png'
		super().__init__(self.image_file, color, initial_position)
		self.nome = 'knight'

	def availableMovePositions(self, table):
		positions = []

		for sum_y in (-2, 2):
			for sum_x in (-1, 1):
				new_position = (self.actualPosition()[0] + sum_x, self.actualPosition()[1] + sum_y)
				other_piece = table.findPiece(new_position)
				if Piece.validPosition(new_position) and (not other_piece or other_piece.color != self.color):
					positions.append(new_position)

		for sum_x in (-2, 2):
			for sum_y in (-1, 1):
				new_position = (self.actualPosition()[0] + sum_x, self.actualPosition()[1] + sum_y)
				other_piece = table.findPiece(new_position)
				if Piece.validPosition(new_position) and (not other_piece or other_piece.color != self.color):
					positions.append(new_position)

		return positions