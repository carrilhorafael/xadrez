from classes.player import Player
from classes.front import Front
from PPlay.mouse import *
from PPlay.window import *
from PPlay.keyboard import *

from main import main

janela = Window(1300, 680)
janela.set_title('Xadrez')
janela.set_background_color((0, 0, 0))

# player_name = input("Digite seu nome de usuário: ")
# player_color = int(input('Selecione a cor que pretende jogar: \n0 - brancas | 1 - pretas\n'))
# while player_color not in [0, 1]:
# 	print('escolha invalida')
# 	player_color = int(input('Selecione a cor que pretende jogar: \n0 - brancas | 1 - pretas'))

player_name = 'pedro'
player_color = 0

player1_color = 'black' if player_color else 'white'
player2_color = 'white' if player_color else 'black'

front = Front(Mouse(), Keyboard())

players = [Player(False, player1_color, player_name), Player(True, player2_color, 'IA')]
players.sort(reverse=True, key=lambda player: player.color == 'white')

main(janela, front, players)
# while True:
# 	front.verifyMouse(janela)
# 	janela.update()