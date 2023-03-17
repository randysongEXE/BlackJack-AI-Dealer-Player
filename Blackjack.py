import random
import pickle

class Blackjack:
    def __init__(self, num_players=1, alpha=0.1, gamma=0.9, epsilon=0.1, load_qtable=False, qtable_file=None):
        self.deck = Deck()
        self.players = [Player() for _ in range(num_players)]
        self.dealer = Dealer()
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        if load_qtable:
            self.load_q_table(qtable_file)
        else:
            self.init_q_table()

    def init_q_table(self):
        self.players[0].q_table = {}

    def load_q_table(self, file):
        with open(file, 'rb') as f:
            self.players[0].q_table = pickle.load(f)

    def save_q_table(self, file):
        with open(file, 'wb') as f:
            pickle.dump(self.players[0].q_table, f)

    def play_round(self):
        self.deck.shuffle()
        for player in self.players:
            player.clear_hand()
        self.dealer.clear_hand()
        for _ in range(2):
            for player in self.players:
                player.take_card(self.deck.deal_card())
            self.dealer.take_card(self.deck.deal_card())
        for player in self.players:
            dealer_hand_value = self.dealer.hand[0].rank if self.dealer.hand[0].rank < 10 else 10
            while player.get_action(dealer_hand_value) == 'hit':
                player.take_card(self.deck.deal_card())
                dealer_hand_value = self.dealer.hand[0].rank if self.dealer.hand[0].rank < 10 else 10
            if player.get_hand_value() > 21:
                reward = -1
            elif self.dealer.get_hand_value() > 21 or player.get_hand_value() > self.dealer.get_hand_value():
                reward = 1
            elif player.get_hand_value() == self.dealer.get_hand_value():
                reward = 0
            else:
                reward = -1
            state = player.get_state(dealer_hand_value)[1]
            player.update_q_table(state, 'stand', reward, 'done')
        dealer_hand_value = self.dealer.get_hand_value()
        self.dealer.play(self.deck)
        for player in self.players:
            if player.get_hand_value() <= 21:
                if self.dealer.get_hand_value() > 21 or player.get_hand_value() > self.dealer.get_hand_value():
                    reward = 1
                elif player.get_hand_value() == self.dealer.get_hand_value():
                    reward = 0
                else:
                    reward = -1
                state = player.get_state(dealer_hand_value)[1]
                player.update_q_table(state, 'stand', reward, 'done')

    def play_game(self, num_rounds):
        for i in range(num_rounds):
            self.play_round()
            print('Round', i+1, 'completed')
        self.save_q_table('q_table.pkl')

    def print_q_table(self):
        for state, actions in self.players[0].q_table.items():
            print(state, actions)

if __name__ == '__main__':
    game = Blackjack(num_players=1, alpha=0.1, gamma=0.9, epsilon=0.1, load_qtable=False, qtable_file='q_table.pkl')
    game.play_game(num_rounds=10000)
    game.print_q_table()
