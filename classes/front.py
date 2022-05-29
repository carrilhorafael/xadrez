class Front:
	def __init__(self):
		pass

	def setFixedPositions(self, positions, table_position):
		for i in range(len(positions)):
			for j in range(len(positions[i])):
				x_casa = i * positions[i][j].width + table_position[0]
				y_casa = j * positions[i][j].height + table_position[1]

				x_circle = x_casa + (positions[i][j].width - positions[i][j].circle.width) / 2
				y_circle = y_casa + (positions[i][j].height - positions[i][j].circle.height) / 2

				positions[i][j].set_position(x_casa, y_casa)
				positions[i][j].border.set_position(x_casa, y_casa)
				positions[i][j].circle.set_position(x_circle, y_circle)

	def setPiecePositions(self, positions, pieces):
		for each in pieces:
			piece_position = each.actualPosition()
			# print(piece_position)
			i = piece_position[0]
			j = piece_position[1]

			x_piece = positions[i][j].x + (positions[i][j].width - pieces[i].width) / 2
			y_piece = positions[i][j].y + (positions[i][j].height - pieces[i].height) / 2

			each.set_position(x_piece, y_piece)

			print(positions[i][j].x, positions[i][j].y)
			print(x_piece, y_piece)
			print()

	def drawPositions(self, positions):
		for i in range(len(positions)):
			for j in range(len(positions[i])):
				positions[i][j].draw()

	def drawCircle(self, circle):
		circle.draw()

	def drawBorder(self, border):
		border.draw()

	def drawPieces(self, pieces):
		for each in pieces:
			each.draw()
