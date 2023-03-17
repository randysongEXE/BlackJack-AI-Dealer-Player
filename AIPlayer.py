import random

class AIPlayer(Player):
    def __init__(self, alpha, gamma, epsilon):
        super().__init__()
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}

    def get_state(self, dealer_hand_value):
        player_hand_value = self.get_hand_value()
        if player_hand_value > 21:
            return 'bust', None
        elif player_hand_value == 21:
            return 'blackjack', None
        else:
            return 'active', (player_hand_value, dealer_hand_value)

    def get_action(self, dealer_hand_value):
        state = self.get_state(dealer_hand_value)
        if state[0] == 'bust' or state[0] == 'blackjack':
            return 'stand'
        if state[1] not in self.q_table:
            self.q_table[state[1]] = {'hit': 0, 'stand': 0}
        if random.random() < self.epsilon:
            return random.choice(['hit', 'stand'])
        else:
            if self.q_table[state[1]]['hit'] > self.q_table[state[1]]['stand']:
                return 'hit'
            else:
                return 'stand'

    def update_q_table(self, state, action, reward, next_state):
        if state not in self.q_table:
            self.q_table[state] = {'hit': 0, 'stand': 0}
        if next_state not in self.q_table:
            self.q_table[next_state] = {'hit': 0, 'stand': 0}
        self.q_table[state][action] += self.alpha * (reward + self.gamma * max(self.q_table[next_state].values()) - self.q_table[state][action])
