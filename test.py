from classes.front import Front
from PPlay.window import *
from PPlay.mouse import *
from PPlay.keyboard import *

from classes.player import Player
from main import main

janela = Window(1300, 680)

front = Front(Mouse(), Keyboard())

mocked_configuration = [
	['black_king'],
	[],
	[],
	[],
	[],
	['black_queen', 'black_bishop'],
	['white_pawn'],
	[None, 'white_king']
]

resp = 1
while resp == 1:
	janela.set_background_color((226, 250, 255))
	resp = main(janela, front, initial_configuration=mocked_configuration)

