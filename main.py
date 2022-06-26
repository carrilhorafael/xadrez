import pdb
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
from classes.end_the_game import EndTheGame
from classes.front import Front
from classes.front_menu import black_time_to_play, mainMenu, white_time_to_play
from classes.menu import menu
from classes.player import Player
from classes.table import Table
from utils.endGame import endGame
from utils.prettyOutput import *

def main(janela, front, initial_configuration=None):

	if initial_configuration:
		table = Table((40, 40), initial_configuration)
	else:
		table = Table((40, 40))

	front.setFixedPositions(table.positions, table.self_position)
	players_or_ias = menu(janela, front, table)

	janela.set_background_color((226, 250, 255))
	front.printTable(table)

	players = [Player(players_or_ias[0], 'white', "Jogador Branco"), Player(players_or_ias[1], 'black', 'Jogador Preto')]

	table.players = players

	turn = 0
	while True:
		can_revert = (players_or_ias[0] or players_or_ias[1]) and (len(players[0].historic_played_pieces) >= 1 and len(players[1].historic_played_pieces) >= 1)
		mainMenu(janela)
		front.printTable(table)

		if len(table.playerPieces(playerColor=players[turn].color)) == 1 and len(table.playerPieces(playerColor=players[not turn].color)) == 1:
			endGame(0)
			return 1

		if len(players[turn].possibleMovements(table)) == 0 and players[turn].underCheck(table):
			endGame(1, winner=players[not turn])
			return 1

		if len(players[turn].possibleMovements(table)) == 0 and not players[turn].underCheck(table):
			endGame(0)
			return 1

		#restart_button.draw()
		#if (mouse.is_over_object(restart_button) and mouse.is_button_pressed(1)):
		#	print("ENTROU---------------------------------------------------------")
			#players[0].historic_played_pieces = []
			#players[1].historic_played_pieces = []
			#return 1

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

		janela.update()
		try:
			table.printTable()
			players[turn].makeMove(table, front, janela, can_revert)

			turn = not turn
		except EndTheGame as end_the_game:
			if end_the_game.args[0] == -1:
				return 1
		except Exception:
			pass

