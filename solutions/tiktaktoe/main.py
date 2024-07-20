from search import *
from game import TicTacToe

game=TicTacToe()
limit=20
frist_player=LimitedAlphaBeta(game,limit=limit)
second_player=LimitedAlphaBeta(game,limit=limit)

game.play(player_one=frist_player,player_two=second_player)