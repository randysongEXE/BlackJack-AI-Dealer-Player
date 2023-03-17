# BlackJack, Dealer and AI Player
This application is a simple implementation of the popular card game "Blackjack" in python. Here are the rules:

1. The goal of the game is to have a hand that is worth more than the dealer's hand without going over 21 points.
2. Cards are worth their face value, with face cars (jacks, kings, queens) worth 10 points and aces worth either 1 or 11 (player's choice).
3. The player can request more cards (aka "hit") to try and reach 21 points, but if 21 points is exceeded, the player loses (aka "bust").
4. After the player's turn is over, the dealer will continue to hit until their hand is worth at least 17 points.
5. If the dealer busts, the player automatically wins.
6. If the dealer's hand is worth more than the player's hand without going over 21, the player loses.
7. If the dealer and player have the same number of points on hand, the game is a tie (aka "push").

This application is unique in that it implements an AI Player. The AI uses a technique called "Q-learning" in order to improve over time.
- The AI has an empty "Q-table" that maps out every possible game scenario to a specific value that represents the expected long-term outcome of taking each possible action from that state
- In each round of the game, the AI will analyze the current scenario of the game and search its table to determine the best possible action based on previous outcomes
- After the game ends (either in a win, draw, or loss), the AI updates its table based on the outcome and the difference between its expected outcome and actual outcome
- As the AI plays more games, its table will become more sophisticated, accurate, and efficient, making better decisions

It is important to note, however, that in the first several games played, the "Q-table" will likely not have amassed information about the current state of the game. In this case, the AI will select a random action.

The dealer, on the other hand, is a set algorithm and will always execute the same action based on its constraints.



