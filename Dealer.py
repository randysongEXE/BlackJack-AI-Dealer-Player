class Dealer(Player):
    def __init__(self):
        super().__init__()

    def play(self, deck):
        while self.get_hand_value() < 17:
            self.take_card(deck.deal_card())
