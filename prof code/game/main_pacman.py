from games import PacmanGame
from search import *
from player import *

game = PacmanGame(board=5)
# first_player = Random(game=game)
first_player = LimitedAlphaBeta(game=game, limit=5)
#first_player = Custom(game)
# second_player = Random(game=game)
second_player = LimitedAlphaBeta(game=game, limit=5)

moves = game.play(first_player, second_player)

print(moves)

