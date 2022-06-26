import pdb
from PPlay.sprite import Sprite

def initialMenu(janela):
  janela.set_title('Xadrez')
  janela.draw_text("XADREZ", 889, 11, size=48, color=(0,0,0), font_name="Arial", bold=False, italic=False)
  janela.draw_text("Menu Principal", 913, 115, size=18, color=(0,0,0), font_name="Arial", bold=False, italic=False)

def mainMenu(janela):
  janela.draw_text("XADREZ", 889, 11, size=48, color=(0,0,0), font_name="Arial", bold=False, italic=False)
  janela.draw_text("Vez de:", 774, 180, size=18, color=(0,0,0), font_name="Arial", bold=False, italic=False)

  revert_button = Sprite("./assets/revert_button.png")
  revert_button.set_position(846, 355)
  revert_button.draw()

  restart_button = Sprite("./assets/restart_button.png")
  restart_button.set_position(846, 430)
  restart_button.draw()

def white_time_to_play():
  white_time_to_play = Sprite("./assets/white_time_to_play.png")
  white_time_to_play.set_position(870, 224)
  white_time_to_play.draw()

  black_no_time_to_play = Sprite("./assets/black_no_time_to_play.png")
  black_no_time_to_play.set_position(1010, 224)
  black_no_time_to_play.draw()

def black_time_to_play():
  white_no_time_to_play = Sprite("./assets/white_no_time_to_play.png")
  white_no_time_to_play.set_position(870, 224)
  white_no_time_to_play.draw()

  black_time_to_play = Sprite("./assets/black_time_to_play.png")
  black_time_to_play.set_position(1010, 224)
  black_time_to_play.draw()

def promoteFront(janela): #IMCOMPLETA
  janela.draw_text("PROMOVER PARA", 889, 11, size=48, color=(0,0,0), font_name="Arial", bold=False, italic=False)
