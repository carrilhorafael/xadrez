from classes.front_menu import black_time_to_play, mainMenu, white_time_to_play
from classes.table import Table
from utils.endGame import endGame
from utils.prettyOutput import *

def main(janela, front, players, initial_configuration=None):
	mainMenu(janela)

	if initial_configuration:
		table = Table((0, 0), players, initial_configuration)
	else:
		table = Table((0, 0), players)

	front.setFixedPositions(table.positions, table.self_position)

	turn = 0
	while True:
		front.setPiecePositions(table.positions, table.pieces)

		front.drawPositions(table.positions)
		front.drawPieces(table.pieces)

		if len(table.playerPieces(playerColor=players[turn].color)) == 1 and len(table.playerPieces(playerColor=players[not turn].color)) == 1:
			endGame(0)
			break

		if len(players[turn].possibleMovements(table)) == 0 and players[turn].underCheck(table):
			endGame(1, winner=players[not turn])
			break

		if len(players[turn].possibleMovements(table)) == 0 and not players[turn].underCheck(table):
			endGame(0)
			break

		#restart_button.draw()
		#if (mouse.is_over_object(restart_button) and mouse.is_button_pressed(1)):
		#	print("ENTROU---------------------------------------------------------")
			#players[0].historic_played_pieces = []
			#players[1].historic_played_pieces = []
			#return 1

		janela.update()

		with prettyOutput(FG_GREEN) as out:
			out.write('*******************************************************************************************************************')

		if turn:
			black_time_to_play()
			with prettyOutput(FG_GREEN) as out:
				out.write('Vez de ' + players[turn].name)
		else:
			white_time_to_play()
			with prettyOutput(FG_MAGENTA) as out:
				out.write('Vez de ' + players[turn].name)

		try:
			table.printTable()
			players[turn].makeMove(table, front, janela)

			turn = not turn
		except Exception:
			print('jogada invalida, repita')
