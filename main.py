from PPlay.window import *
from PPlay.sprite import *
from classes.table import Table
from classes.front import Front
from utils.endGame import endGame
from utils.prettyOutput import *

def main(players, initial_configuration=None):
	janela = Window(1300, 680)
	janela.set_title('Xadrez')
	janela.set_background_color((0, 0, 0))

	if initial_configuration:
		table = Table((0, 0), players, initial_configuration)
	else:
		table = Table((0, 0), players)

	# AREA DE TESTES
	casa = Sprite('assets/blackPosition.jpg')
	circle = Sprite('assets/circle.png')
	x = casa.x + (casa.width - circle.width) / 2
	y = casa.y + (casa.height - circle.height) / 2
	circle.set_position(x, y)
	#

	front = Front()
	front.setFixedPositions(table.positions, table.self_position)

	turn = 0
	while True:
		front.setPiecePositions(table.positions, table.pieces)

		front.drawPositions(table.positions)
		front.drawPieces(table.pieces)

		for i in range(len(table.positions)):
			for j in range(len(table.positions[i])):
				front.drawBorder(table.positions[i][j].border)
				front.drawCircle(table.positions[i][j].circle)

		janela.update()
		if len(players[turn].possibleMovements(table)) == 0 and players[turn].underCheck(table):
			endGame(1, winner=players[not turn])
			break

		if len(players[turn].possibleMovements(table)) == 0 and not players[turn].underCheck(table):
			endGame(0)
			break

		if len(table.playerPieces(playerColor=players[turn].color)) == 1 and len(table.playerPieces(playerColor=players[turn].color)) == 1:
			endGame(0)
			break

		with prettyOutput(FG_GREEN) as out:
			out.write('*******************************************************************************************************************')

		if not players[turn].system_controlled:
			with prettyOutput(FG_GREEN) as out:
				out.write('Vez de ' + players[turn].name)
		else:
			with prettyOutput(FG_MAGENTA) as out:
				out.write('Jogada de ' + players[turn].name)

		table.printTable()
		try:
			players[turn].makeMove(table)

			turn = not turn
		except Exception:
			print('jogada invalida, repita')