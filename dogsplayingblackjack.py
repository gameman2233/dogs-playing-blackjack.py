# dogs playing INFINITE HAND BLACKJACK .py
import random
#important variables
options = ("")
suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
numbers = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","King","Queen","Jack"]

# Player and Dealer player classes
class player:
    cards_handed = []
    score = 0
    has_ace = 0
    can_double = False
    chips = 5000
    bet = 0
class dealer:
    cards_handed = []
    score = 0
    has_ace = 0
#draws a card from the deck for the player, 
def hit():
    clear()
    dog_dealer()
    chip_display()
    dealer_cards = (" ").join(dealer.cards_handed[0])
    print(dealer_cards)
    print("(card hidden)")
    print("--------------")
    for x in range(len(player.cards_handed)):
        print ((" ").join(player.cards_handed[x]))
    random_card(player)
    print(player.score)
    if player.score > 21:
        player_lose()
#ends players turn and begins dealers turn
def stand():
    clear()
    dog_dealer()
    chip_display()
    for x in range(len(dealer.cards_handed)):
        print ((" ").join(dealer.cards_handed[x]))
    while dealer.score < 17:
        random_card(dealer)
    print(dealer.score)
    print("--------------")
    for x in range(len(player.cards_handed)):
        print ((" ").join(player.cards_handed[x]))
    print(player.score)
    if(dealer.score > player.score and dealer.score < 22):
        player_lose()
    elif player.score > 21:
        player_lose()
    elif player.score == dealer.score:
        push()
    else:
        player_win()
# Self-explanatory, player win event
def player_win():
    print("You win!")
    player.chips = player.chips + player.bet*2
    print("New chips:", player.chips)
# Blackjack pays 3:1, if you get a 10 or face and an ace, you win round 1 
def turn_one_win():
    print("You win!")
    player.chips = player.chips + player.bet*2
    player.chips = player.chips + player.bet
    print("New chips:", player.chips)
    player.bet = 0
# Loss on turn one and showing dealer's cards
def turn_one_loss():
    clear()
    dog_dealer()
    for x in range(len(dealer.cards_handed)):
        print ((" ").join(dealer.cards_handed[x]))    
    chip_display()
    print(dealer.score)
    print("--------------")
    for x in range(len(player.cards_handed)):
        print ((" ").join(player.cards_handed[x]))
    print(player.score)
    player_lose()
# Tie State
def push():
    print("Push")
    player.chips = player.chips + player.bet
    print("New chips:", player.chips)
    player.bet = 0
# Lose State
def player_lose():
    print("You lose.")
    print("New chips:", player.chips)
    player.bet = 0
# Displays player's chips
def chip_display():
    print("Chips:",player.chips,"      Bet:",player.bet)
# Clears the screen, first piece of code implemented
def clear():
    print ("\033c")
# Dog ascii art from https://www.asciiart.eu/animals/dogs Cocoa
def dog_dealer():
    print("     /^ ^\\")
    print("    / 0 0 \\")
    print("    V\\ Y /V")
    print("     / - \\")
    print("     |    \\")
    print("     || (__V")
    print("--------------------")
# Used to draw a card from the deck
def random_card(user):
    suit_rand=random.choice(suits)
    num_rand=random.choice(numbers)
    print(num_rand,"of",suit_rand)
    user.cards_handed.append([num_rand, "of", suit_rand])
    if num_rand == "Ace":
        user.score = user.score + 11
        user.has_ace = user.has_ace + 1
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
    if user.has_ace > 0 and user.score > 21:
        user.score = user.score - 10
        user.has_ace = user.has_ace - 1
# Used to draw the dealer's second card on game start
def hidden_card(user):
    suit_rand=random.choice(suits)
    num_rand=random.choice(numbers)
    print("(card hidden)")
    user.cards_handed.append([num_rand, "of", suit_rand])
    if num_rand == "Ace":
        user.score = user.score + 11
        user.has_ace = user.has_ace + 1
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
    if user.has_ace >0 and user.score > 21:
        user.score = user.score - 10
        user.has_ace = user.has_ace - 1
# Game Start
def turn_one(user):
    random_card(user)
    if user == dealer:
        hidden_card(user)
    else:
        random_card(user) 
# Resets all variables and prompts user for a bet
def prep():
    player.cards_handed = []
    dealer.cards_handed = []
    player.score = 0
    dealer.score = 0
    player.has_ace = False
    dealer.has_ace = False
    player.can_double
    while True:
        player.bet = 0
        chip_display()
        try:
            bet = int(input("How much would you like to bet? "))
            if bet > player.chips:
                clear()
                print("You don't have enough chips for that.")
                continue
            if bet < 0:
                clear()
                print("Please use positive integers only")
                continue
        except(ValueError):
            clear()
            print("Please use positive integers only.")
            continue
        else:
            player.bet = bet
            player.chips = player.chips - bet
            clear()
            break
# Plays blackjack
def play():
    while True:
        while True:
            prelude = input("Would you like to play blackjack?, Select Yes or No: ")
            if prelude == "Yes":
                clear()
                prelude = ""
                break
            elif prelude == "No":
                break
        if prelude == "No":
            clear()
            break
        prep()
        game_in_progress = True
        dog_dealer()
        chip_display()
        turn_one(dealer)
        print("--------------")
        turn_one(player)
        print(player.score)
        if dealer.score == 21 and dealer.score != player.score:
            turn_one_loss()
            continue
        elif player.score == 21 and dealer.score != player.score:
            print("Player wins.")
            turn_one_win()
            continue
        elif player.score == 21 and dealer.score == 21:
            push()
        if (player.score == 9 or player.score == 10 or player.score == 11) and (player.has_ace == False) or (player.score == 16 or player.score == 17 or player.score == 18) and (player.has_ace == True):
            options = input("Would you like to Hit, Stand or Double? ")
            player.can_double = True
        else:
            options = input("Would you like to Hit or Stand? ")
        while True:
            if options == "Double" and player.can_double == True:
                if player.chips > player.bet:
                    player.bet = player.bet * 2
                    hit()
                    options = "Stand"
                else:
                    print("You can not afford to double.")
            if options == "Stand":
                break
            if options == "Hit":
                hit()
                options = (" ")
            if player.score >=22:
                player_lose()
                break
            options = input("Would you like to Hit or Stand? ")
            
        stand()



play()
