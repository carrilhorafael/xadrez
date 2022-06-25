from pickle import TRUE
from PPlay import mouse
from PPlay.sprite import Sprite

mouse = mouse.Mouse()

def menu(janela):
  janela.draw_text("Menu Principal", 913, 115, size=18, color=(0,0,0), font_name="Arial", bold=False, italic=False)

  white_piece_allow = Sprite("./assets/white_piece_allow.png")
  white_piece_unable = Sprite("./assets/white_piece_unable.png")
  black_piece_allow = Sprite("./assets/black_piece_allow.png")
  black_piece_unable = Sprite("./assets/black_piece_unable.png")

  play_button = Sprite("./assets/play_button.png")

  white_piece_allow.set_position(846, 250)
  white_piece_unable.set_position(846, 250)
  black_piece_allow.set_position(1066, 250)
  black_piece_unable.set_position(1066, 250)

  play_button.set_position(846, 554)

  white_piece_allow.draw()
  black_piece_unable.draw()
  play_button.draw()

  players = [False, True]

  while 1:

    if (mouse.is_over_object(white_piece_allow) and mouse.is_button_pressed(1)):
      if not players[0]:
        players[0] = True
        white_piece_unable.draw()
      else:
        players[0] = False
        white_piece_allow.draw()

    if (mouse.is_over_object(black_piece_unable) and mouse.is_button_pressed(1)):
      if not players[1]:
        players[1] = True
        black_piece_unable.draw()
      else:
        players[1] = False
        black_piece_allow.draw()

    if (mouse.is_over_object(play_button) and mouse.is_button_pressed(1)):
      break

    janela.update()


  janela.clear()
  return players