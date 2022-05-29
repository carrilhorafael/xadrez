from classes.player import Player
from main import main


# player_name = input("Digite seu nome de usuário: ")
# player_color = int(input('Selecione a cor que pretende jogar: \n0 - brancas | 1 - pretas\n'))
# while player_color not in [0, 1]:
# 	print('escolha invalida')
# 	player_color = int(input('Selecione a cor que pretende jogar: \n0 - brancas | 1 - pretas'))

player_name = 'pedro'
player_color = 0

player1_color = 'black' if player_color else 'white'
player2_color = 'white' if player_color else 'black'

players = [Player(False, player1_color, player_name), Player(True, player2_color)]
players.sort(reverse=True, key=lambda player: player.color == 'white')

main(players)
