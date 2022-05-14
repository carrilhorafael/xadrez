class Player:
  def __init__(self, system_controlled, color, name="IA"):
    self.system_controlled = system_controlled
    self.name = name
    self.color = color

  def choosePiece(self, table):
    piece = None
    while not piece:
      piece_entry = tuple(map(int, input("Escolha as coordenadas de uma peça (x, y): ").split(" ")))
      piece = table.findPiece(piece_entry, self.color)
      if piece == None:
        print("Jogada inválida")
    return piece

  def makeMove(self, piece, table):
    position_entry = tuple(map(int, input('Insira a coordenada para se movimentar (x, y): ').split(" ")))
    piece.move(position_entry, table)

  def possibleMoviments(self, table):
    return_possibilities = []
    for piece in table.playerPieces(self.color):
      piece_available_positions = piece.availablePositions(table)
      if len(piece_available_positions) > 0:
        return_possibilities.append((piece, piece_available_positions))
    return return_possibilities

