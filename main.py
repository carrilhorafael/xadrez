from PPlay.window import *
from classes.table import Table
from utils.endGame import endGame
from utils.prettyOutput import *

def main(players, initial_configuration=None):
  janela = Window(1920, 1040)
  janela.set_title('Xadrez')
  if initial_configuration:
    table = Table((300, 300), players, initial_configuration)
  else:
    table = Table((300, 300), players)


  turn = 0

  while True:
    if len(players[turn].possibleMovements(table)) == 0:
      endGame(0)
      break

    with prettyOutput(FG_GREEN) as out:
      out.write('*******************************************************************************************************************')

    if not players[turn].system_controlled:
      with prettyOutput(FG_GREEN) as out:
        out.write('Vez de ' + players[turn].name)
    else:
      with prettyOutput(FG_MAGENTA) as out:
        out.write('Jogada de ' + players[turn].name)

    table.printTable()
    try:
      players[turn].makeMove(table)

      if players[not turn].king(table) == None:
        endGame(1, winner=players[turn])
        break

      turn = not turn
    except Exception:
      print('jogada invalida, repita')
