class Front:
	def __init__(self, mouse, keyboard):
		self.mouse = mouse
		self.keyboard = keyboard

		self.valid = True

	def setFixedPositions(self, positions, table_position):
		for i in range(len(positions)):
			for j in range(len(positions[i])):
				x_casa = i * positions[i][j].width + table_position[0]
				y_casa = j * positions[i][j].height + table_position[1]

				x_circle = x_casa + (positions[i][j].width - positions[i][j].circle.width) / 2
				y_circle = y_casa + (positions[i][j].height - positions[i][j].circle.height) / 2

				positions[i][j].set_position(x_casa, y_casa)
				positions[i][j].attack_circle.set_position(x_casa, y_casa)
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

			# print(positions[i][j].x, positions[i][j].y)
			# print(x_piece, y_piece)
			# print()

	def drawPositions(self, positions):
		for i in range(len(positions)):
			for j in range(len(positions[i])):
				positions[i][j].draw()

	def drawCircles(self, positions):
		for i in range(len(positions)):
			for j in range(len(positions[i])):
				if positions[i][j].isUnderAttack:
					positions[i][j].attack_circle.draw()
					positions[i][j].isUnderAttack = False
				elif positions[i][j].isCircleOn:
					positions[i][j].circle.draw()
					positions[i][j].isCircleOn = False
			# 	positions[i][j].isCircleOn = False
				# if positions[i][j].isCircleOn:
				# 	positions[i][j].circle.draw()
				# 	positions[i][j].isCircleOn = False

	def drawBorder(self, border):
		border.draw()

	def drawPieces(self, pieces):
		for each in pieces:
			each.draw()

	def setCirclesOn(self, piece, table):
		#available_positions = piece.availabePositions(table)
		available_positions = table.filterAvailablePositions(piece)
		#print(available_positions)
		for i in range(len(available_positions)):
				x = available_positions[i][0][0]
				y = available_positions[i][0][1]
				pieceUnderAttack = available_positions[i][1]
				#print('x:', x, ' y:', y)
		# 	x = available_positions[i][0]
		# 	y = available_positions[i][1]
				table.positions[x][y].isCircleOn = True
				if pieceUnderAttack is not None:
					table.positions[x][y].isUnderAttack = True

	def verifyMouse(self, janela):
		if self.valid and self.mouse.is_button_pressed(1):
			janela.set_background_color((255, 255, 255))
			self.valid = False

		if not self.valid and self.mouse.is_button_pressed(1):
			janela.set_background_color((0, 0, 0))
			self.valid = True
