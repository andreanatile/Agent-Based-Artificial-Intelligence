
from games import *
from search import *
"""game = DummyGame()
first_player = Minimax(game=game)
second_player = Minimax(game=game)

state = game.initial_state
moves = game.play(first_player, second_player)

print(moves)
"""

game=TicTacToe()
first_player=Minimax(game=game)
second_player=Minimax(game=game)

state=game.initial_state
moves=game.play(first_player,second_player)
print(moves)

