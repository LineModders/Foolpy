import random

print('Welcome, pls visit github! - github.com/LineModders')
    
# Create a deck of cards
suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
ranks = ['6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [(rank, suit) for suit in suits for rank in ranks]

# Shuffle the deck
random.shuffle(deck)

# Deal cards to players
player_hand = [deck.pop() for _ in range(6)]
computer_hand = [deck.pop() for _ in range(6)]

# Main game loop
while len(deck) > 0 or len(player_hand) > 0 or len(computer_hand) > 0:
    # Check if player or computer has no cards left
    if len(player_hand) == 0 or len(computer_hand) == 0:
        break
    
    # Player's turn
    print('Your hand:')
    for i, card in enumerate(player_hand):
        print(f'{i+1}. {card[0]} of {card[1]}')

    selected_card_index = int(input('Select a card to play (enter the number): ')) - 1
    selected_card = player_hand[selected_card_index]
    player_hand.remove(selected_card)
    
    # Computer's turn
    computer_card = random.choice(computer_hand)
    computer_hand.remove(computer_card)
    
    # Check who wins the round
    if ranks.index(selected_card[0]) > ranks.index(computer_card[0]):
        print('You win the round!')
        player_hand.append(selected_card)
        player_hand.append(computer_card)
    else:
        print('Computer wins the round!')
        computer_hand.append(selected_card)
        computer_hand.append(computer_card)
    
# Game over
print('Game over!')
if len(player_hand) > len(computer_hand):
    print('You win!')
elif len(player_hand) < len(computer_hand):
    print('You lose!')
else:
    print('It\'s a tie!')