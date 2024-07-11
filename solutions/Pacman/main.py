from game import PacMan
from search import *


game=PacMan(board_size=5)

player1=AlphaBetaLimited(game,limit=10)
player2 = AlphaBetaLimited(game, limit=10)

game.play(player_one=player1, player_two=player2)
