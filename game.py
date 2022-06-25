from classes.front_menu import menu
from classes.player import Player
from classes.front import Front
from PPlay.mouse import *
from PPlay.window import *
from PPlay.keyboard import *

from main import main

janela = Window(1300, 680)
janela.set_title('Xadrez')
janela.set_background_color((226, 250, 255))
janela.draw_text("XADREZ", 889, 11, size=48, color=(0,0,0), font_name="Arial", bold=False, italic=False)

players_or_ias = menu(janela)

# player_name = input("Digite seu nome de usuário: ")
# player_color = int(input('Selecione a cor que pretende jogar: \n0 - brancas | 1 - pretas\n'))
# while player_color not in [0, 1]:
# 	print('escolha invalida')
# 	player_color = int(input('Selecione a cor que pretende jogar: \n0 - brancas | 1 - pretas'))

player_color = 0

player1_color = 'black' if player_color else 'white'
player2_color = 'white' if player_color else 'black'

front = Front(Mouse(), Keyboard())

players = [Player(players_or_ias[0], player1_color, "Jogar Branco"), Player(players_or_ias[1], player2_color, 'Jogador Preto')]
players.sort(reverse=True, key=lambda player: player.color == 'white')

main(janela, front, players)
# while True:
# 	front.verifyMouse(janela)
# 	janela.update()
