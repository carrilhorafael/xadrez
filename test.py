from classes.front import Front
from classes.player import Player
from PPlay.window import *
from PPlay.mouse import *
from PPlay.keyboard import *

from classes.player import Player
from main import main

janela = Window(1300, 680)
janela.set_title('Xadrez')
janela.set_background_color((0, 0, 0))

front = Front(Mouse(), Keyboard())

mocked_configuration = [
  ['black_rook', 'black_knight', 'black_bishop', 'black_queen', None, 'black_bishop', None, None],
  ['black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'white_pawn', 'white_pawn'],
  [],
  ['white_king'],
  [],
  ['black_king'],
  ['white_pawn', None, 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn'],
  ['white_rook', None, None, None, None, None, None, 'white_rook']
]

players = [Player(True, 'white', 'IA 1'), Player(True, 'black', 'IA 2')]
main(janela, front, players, initial_configuration=mocked_configuration)
