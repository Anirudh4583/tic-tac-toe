from game import Game
from qLearning import QAgent
import random as rd


def play(agent):
    game = Game(log=True)
    while True:
        action = agent.q.get_best_move(game.get_grid())
        winner = game.play(*action) if action else game.play(*
                                                             rd.choice(game.get_actions()))
        if winner:
            print("LOOSER!")
            return
        if game.is_over():
            print("DRAW")
            return

        row, col = input("Enter row and col: ").split()
        winner = game.play(int(row), int(col))
        if winner:
            print("WINNER!")
            return
        if game.is_over():
            print("DRAW")
            return


agent = QAgent()
print("Started Learning")
agent.train(times=20000)
print("Finished Learning")


while True:
    play(agent)
    print("Play again? (y/n)")
    if input() == 'n' or input() == 'N':
        break
