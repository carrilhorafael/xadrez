from PPlay.window import *
from PPlay.sprite import *

janela = Window(720, 1440)
janela.set_title('Xadrez')
close = False
piece = Sprite('./assets/horse.png', frames=1)

while not close:
  piece.move_key_x(0.1)
  piece.move_key_y(0.1)
  janela.set_background_color((255,255,255))
  piece.draw()
  janela.update()
