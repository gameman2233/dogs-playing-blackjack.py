# dogs playing INFINITE HAND BLACKJACK .py
import random
options = ("")
suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
numbers = ["Ace",2,3,4,5,6,7,8,9,10]
chips = 5000
class player:
    cards_handed = []
    score = 0
    has_ace = False
class dealer:
    cards_handed = []
    score = 0
    has_ace = False
def clear():
    print ("\033c")
def dog_dealer():
    print("     /^ ^\\")
    print("    / 0 0 \\")
    print("    V\\ Y /V")
    print("     / - \\")
    print("     |    \\")
    print("     || (__V")
    print("--------------------")

def random_card(user):
    suit_rand=random.choice(suits)
    num_rand=random.choice(numbers)
    print(num_rand,"of",suit_rand)
    user.cards_handed.append([num_rand, "of", suit_rand])
    if num_rand == "Ace":
        user.score = user.score + 11
        user.has_ace = True
    else:
        user.score = user.score + num_rand
def hidden_card(user):
    suit_rand=random.choice(suits)
    num_rand=random.choice(numbers)
    print("(card hidden)")
    user.cards_handed.append([num_rand, "of", suit_rand])
    if num_rand == "Ace":
        user.score = user.score + 11
        user.has_ace = True
    else:
        user.score = user.score + num_rand
def turn(user):
    random_card(user)
    if user == dealer:
        hidden_card(user)
    else:
        random_card(user)
def prep():
    player.score = 0
    dealer.score = 0
    player.has_ace = False
    dealer.has_ace = False
def play():
    while True:
        prep()
        game_in_progress = True
        dog_dealer()
        turn(dealer)
        turn(player)
        print(player.score)
        print(player.cards_handed)
        if dealer.score == 21:
            print("Dealer wins.")
        elif player.score == 21:
            print("Player wins.")
        if (player.score == 9 or player.score == 10 or player.score == 11) and (player.has_ace == False) or (player.score == 16 or player.score == 17 or player.score == 18) and (player.has_ace == True):
            options = input("Would you like to Hit, Stand or Double?")
        else:
            options = input("Would you like to Hit or Stand?")
        if options == "Hit":
            clear()
            dog_dealer()
            dealer_cards = (" ").join(dealer.cards_handed[0])
            print(dealer_cards)
            break

        

play()
