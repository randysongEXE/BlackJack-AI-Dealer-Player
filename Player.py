class Player:
    def __init__(self):
        self.hand = []

    def get_hand_value(self):
        hand_value = 0
        for card in self.hand:
            if card.rank == 1:
                hand_value += 11
            elif card.rank in [11, 12, 13]:
                hand_value += 10
            else:
                hand_value += card.rank
        num_aces = sum([1 for card in self.hand if card.rank == 1])
        while num_aces > 0 and hand_value > 21:
            hand_value -= 10
            num_aces -= 1
        return hand_value

    def take_card(self, card):
        self.hand.append(card)
