from classes.front import Front
from classes.player import Player
from PPlay.window import *
from PPlay.mouse import *
from PPlay.keyboard import *
from main import main

janela = Window(1300, 680)
janela.set_title('Xadrez')
janela.set_background_color((0, 0, 0))

front = Front(Mouse(), Keyboard())

mocked_configuration = [
  ['black_rook', 'black_knight', 'black_bishop', 'black_queen', 'black_king', 'black_bishop', 'black_knight', 'black_rook'],
  ['black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn'],
  [],
  [],
  [None, 'white_pawn'],
  [],
  ['white_pawn', None, 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn'],
  ['white_rook', 'white_knight', 'white_bishop', 'white_queen', 'white_king', 'white_bishop', 'white_knight', 'white_rook']
]

players = [Player(True, 'white', 'IA 1'), Player(True, 'black', 'IA 2')]
main(janela, front, players, initial_configuration=mocked_configuration)
