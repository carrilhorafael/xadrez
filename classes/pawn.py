from classes.piece import Piece

class Pawn (Piece):
	def __init__(self, color, initial_position):
		self.image_file = './assets/' + color + 'Pawn.png'
		super().__init__(self.image_file, color, initial_position)
		self.nome = 'pawn'

	def availableMovePositions(self, table):
		positions = []
		if self.color == 'black':
			if len(self.historic_positions) > 1:
				new_position = (self.actualPosition()[0], self.actualPosition()[1] + 1)
				if Piece.validPosition(new_position) and not table.findPiece(new_position):
					positions.append(new_position)
			else:
				for i in range(1, 3, 1):
					new_position = (self.actualPosition()[0], self.actualPosition()[1] + i)
					if Piece.validPosition(new_position) and not table.findPiece(new_position):
						positions.append(new_position)
		else:
			if len(self.historic_positions) > 1:
				new_position = (self.actualPosition()[0], self.actualPosition()[1] - 1)
				if Piece.validPosition(new_position) and not table.findPiece(new_position):
					positions.append(new_position)
			else:
				for i in range(1, 3, 1):
					new_position = (self.actualPosition()[0], self.actualPosition()[1] - i)
					if Piece.validPosition(new_position) and not table.findPiece(new_position):
						positions.append(new_position)

		return positions