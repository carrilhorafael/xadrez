from classes.menu import menu
from classes.player import Player
from classes.front import Front
from PPlay.mouse import *
from PPlay.window import *
from PPlay.keyboard import *

from main import main

janela = Window(1300, 680)

front = Front(Mouse(), Keyboard())

resp = 1
while resp:
  janela.set_background_color((226, 250, 255))
  resp = main(janela, front)
