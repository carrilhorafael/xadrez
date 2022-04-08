from PPlay.window import *
from PPlay.sprite import *
from classes.position import Position
from classes.table import Table

janela = Window(1440, 720)
janela.set_title('Xadrez')

table = Table((70, 70), 512)

while True:
  table.printTable()
  janela.update()
