class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['hearts', 'diamonds', 'clubs', 'spades']:
            for rank in range(1, 14):
                self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
