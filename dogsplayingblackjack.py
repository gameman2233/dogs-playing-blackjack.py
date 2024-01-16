# dogs playing INFINITE HAND BLACKJACK .py
import random
options = ("")
suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
numbers = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","King","Queen","Jack"]
chips = 5000
class player:
    cards_handed = []
    score = 0
    has_ace = False
    can_double = False
class dealer:
    cards_handed = []
    score = 0
    has_ace = False
def hit():
    dog_dealer()
    dealer_cards = (" ").join(dealer.cards_handed[0])
    print(dealer_cards)
    print("(card hidden)")
    for x in range(len(player.cards_handed)):
        print ((" ").join(player.cards_handed[x]))
    random_card(player)
    print(player.score)
def player_lose():
    
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
    elif num_rand == "King":
        user.score = user.score + 10
    elif num_rand == "Queen":
        user.score = user.score + 10
    elif num_rand == "Jack":
        user.score = user.score + 10
    elif num_rand == "Two":
        user.score = user.score + 2
    elif num_rand == "Three":
        user.score = user.score + 3
    elif num_rand == "Four":
        user.score = user.score + 4
    elif num_rand == "Five":
        user.score = user.score + 5
    elif num_rand == "Six":
        user.score = user.score + 6
    elif num_rand == "Seven":
        user.score = user.score + 7
    elif num_rand == "Eight":
        user.score = user.score + 8
    elif num_rand == "Nine":
        user.score = user.score + 9
    elif num_rand == "Ten":
        user.score = user.score + 10    
    if user.has_ace == True and user.score > 21:
        user.score = user.score - 10
        user.has_ace = False
def hidden_card(user):
    suit_rand=random.choice(suits)
    num_rand=random.choice(numbers)
    print("(card hidden)")
    user.cards_handed.append([num_rand, "of", suit_rand])
    if num_rand == "Ace":
        user.score = user.score + 11
        user.has_ace = True
    elif num_rand == "King":
        user.score = user.score + 10
    elif num_rand == "Queen":
        user.score = user.score + 10
    elif num_rand == "Jack":
        user.score = user.score + 10
    elif num_rand == "Two":
        user.score = user.score + 2
    elif num_rand == "Three":
        user.score = user.score + 3
    elif num_rand == "Four":
        user.score = user.score + 4
    elif num_rand == "Five":
        user.score = user.score + 5
    elif num_rand == "Six":
        user.score = user.score + 6
    elif num_rand == "Seven":
        user.score = user.score + 7
    elif num_rand == "Eight":
        user.score = user.score + 8
    elif num_rand == "Nine":
        user.score = user.score + 9
    elif num_rand == "Ten":
        user.score = user.score + 10    
    if user.has_ace == True and user.score > 21:
        user.score = user.score - 10
        user.has_ace = False
def turn_one(user):
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
        turn_one(dealer)
        turn_one(player)
        print(player.score)
        print(player.cards_handed)
        if dealer.score == 21:
            print("Dealer wins.")
        elif player.score == 21:
            print("Player wins.")
        if (player.score == 9 or player.score == 10 or player.score == 11) and (player.has_ace == False) or (player.score == 16 or player.score == 17 or player.score == 18) and (player.has_ace == True):
            options = input("Would you like to Hit, Stand or Double?")
            player.can_double = True
        else:
            options = input("Would you like to Hit or Stand?")
        while player.score < 22:
            if options == "Hit":
                hit()
                options = (" ")
            if player.score >=22:
                player_lose()
            options = input("Would you like to Hit or Stand?")



play()
