import random
import time

card_suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
card_list = ["Ace", "2", '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', "Queen", "King"]
money = 100

def new_deck():
    deck = [(card, suit) for card in card_list for suit in card_suits]
    random.shuffle(deck)
    return deck

def card_value(card):
    if card[0] in ["Jack", "Queen", "King"]:
        return 10
    elif card[0] == "Ace":
        return 11
    else:
        return int(card[0])
    
def hand_value(hand):
    total = sum(card_value(card) for card in hand)
    aces = sum(1 for card in hand if card[0] == "Ace")
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total
 
def card_str(card):
    return card[0] + " of " + card[1]

def hand_str(hand):
    return ", ".join(card_str(card) for card in hand)

def print_scores(hide_card = False):
    print("Player shows " + hand_str(player_hand))
    time.sleep(0.5)
    print("Player total: " + str(player_score))
    time.sleep(1)

    if hide_card:
        print("Dealer shows " + card_str(dealer_hand[0]))
        time.sleep(1)
    else:
        print("Dealer shows " + hand_str(dealer_hand))
        time.sleep(0.5)
        print("Dealer total: " + str(dealer_score))
        time.sleep(1)

print("--BLACKJACK--")
time.sleep(1)

while True:
    deck = new_deck()
    winner = ""

    while True:
        try:
            bet = int(input("You have $" + str(money) + ", how much would you like to bet?\n"))
        except ValueError:
            print("Please enter a whole number")
            continue
        
        if bet > money:
            print("You don't have enough to bet that much")
        elif bet < 1:
            print("that is not a valid amount")
        else:
            print("You bet $" + str(bet))
            money -= bet
            time.sleep(0.5)
            break

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    while True:
        player_score = hand_value(player_hand)
        dealer_score = hand_value(dealer_hand)
        print_scores(hide_card=True)
        
        if player_score > 21:
            print("You bust, you lose")
            winner = "dealer"
            break

        choice = input("Would you like to hit(h) or stand(s)\n")
        if choice == "h":
            new_card = deck.pop()
            print("You draw the " + card_str(new_card))
            time.sleep(1)
            player_hand.append(new_card)
        elif choice == "s":
            print("You stand")
            break
        else:
            print("Invalid input")

    if player_score <= 21:  
        print("Dealer flips over the " + card_str(dealer_hand[1]))
        time.sleep(1)
        print_scores()

        while dealer_score < 17:
            print("Dealer hits")
            time.sleep(0.5)
            new_card = deck.pop()
            print("Dealer draws the " + card_str(new_card))
            time.sleep(1)
            dealer_hand.append(new_card)
            dealer_score = hand_value(dealer_hand)
            print_scores()

        if dealer_score > 21:
            print("Dealer busts, you win")
            winner = "player"
        elif player_score > dealer_score:
            print("You win")
            winner = "player"
        elif player_score == dealer_score:
            print("Push")
            winner = "tie"
        else:
            print("You lose")
            winner = "dealer"

    if winner == "player":
        money += 2 * bet
    elif winner == "tie":
        money += bet
    
    print("You have $" + str(money))

    if money <= 0:
        print("You've lost all your money")
        break
    else:
        while True:
            play = input("Would you like to play again? (y/n)\n")
            if play == "y" or play == "n": 
                break
            else:
                print("Invalid input")
        if play == "n":
            break
