class Player:
  def __init__(self, system_controlled, color, name="IA"):
    self.system_controlled = system_controlled
    self.name = name
    self.color = color

  def makeMove():
    input("Escolha as coordenadas de uma peça (x, y): ").split(" ")

  def choosePiece(self, table):
    piece = None
    while not piece:
      piece_entry = tuple(map(int, input("Escolha as coordenadas de uma peça (x, y): ").split(" ")))
      piece = table.findPiece(piece_entry, self.color)
      if piece == None:
        print("Jogada inválida")
    return piece

