from collections import defaultdict
import random as rd
from game import Game

# Class QLearning


class QLearning:
    def __init__(self, dis=0.5, a=0.5):
        self.dis = dis
        self.a = a
        self.q = defaultdict(lambda: defaultdict(lambda: 0.0))

    # function to update Q-Table
    def next(self, action, reward, state, next_state):
        # Q0 = R0
        q_curr = self.q[state][action]
        temp = list(self.q[next_state].values())
        q_next = max(temp) if temp else 0
        # Qn = Qn-1 + a(Rn + dis * Qn+1 - Qn-1)
        q_curr = q_curr + self.a * (reward + self.dis * q_next - q_curr)
        self.q[state][action] = q_curr

    # function to get the best move
    def get_best_move(self, state):
        temp = list(self.q[state].keys())
        return max(temp, key=lambda p: self.q[state][p]) if temp else None

# QLearning Agent


class QAgent:
    def __init__(self):
        self.epsilon = 1.0
        self.q = QLearning()

    # function to get the best move
    def get_action(self, state, valid_actions):
        best_move = self.q.get_best_move(state)
        if rd.random() < self.epsilon or best_move is None:
            return rd.choice(valid_actions)
        return best_move

    def learn(self):
        game = Game()
        while True:
            state = game.get_grid()
            valid_actions = game.get_actions()
            action = self.get_action(state, valid_actions)
            winner = game.play(*action)

            # win
            if winner or game.is_over():
                self.q.next(action, 100, state, game.get_grid())
                break

            # lose
            winner = game.play(*rd.choice(game.get_actions()))
            if winner or game.is_over():
                self.q.next(action, -100, state, game.get_grid())
                break
            # draw
            self.q.next(action, 0, state, game.get_grid())

    def train(self, times):
        for _ in range(times):
            self.learn()
            self.epsilon -= 0.0001
