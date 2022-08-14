import random

computer_cards_template = [11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8 ,8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
human_cards_template = ["A♣", "A♥", "A♠", "A♦", "2♣", "2♥", "2♠", "2♦", "3♣", "3♥", "3♠", "3♦", "4♣", "4♥", "4♠", "4♦", "5♣", "5♥", "5♠", "5♦", "6♣", "6♥", "6♠", "6♦", "7♣", "7♥", "7♠", "7♦", "8♣", "8♥", "8♠", "8♦", "9♣", "9♥", "9♠"," 9♦", "10♣", "10♥", "10♠", "10♦", "J♣", "J♥", "J♠", "J♦", "Q♣", "Q♥", "Q♠", "Q♦", "K♣", "K♥", "K♠", "K♦"]

deck_amount = 1
difficulty = 0
running_count = 0

computer_cards = []
human_cards = []

def check_and_shuffle(running_count):
    if len(computer_cards) < len(computer_cards_template) * deck_amount / 2:
        template_to_cards(deck_amount)
        print("The deck has been shuffled")
        return 0
    else:
        return running_count

def template_to_cards(deck_amount):
    for i in range(deck_amount):
        computer_cards.extend(computer_cards_template)
        human_cards.extend(human_cards_template)

def print_cards(dealer_cards, user_cards):
    print(f"\nDealer's cards:\n{dealer_cards[0]} _\nYour cards:\n{' '.join(user_cards)}")

def print_cards_real(dealer_cards, user_cards):
    print(f"\nDealer's cards:\n{' '.join(dealer_cards)}\nYour cards:\n{' '.join(user_cards)}")

def to_count_value(a):
    if a <= 6:
        return 1
    elif a >= 10:
        return -1
    else:
        return 0

def blackjack(balance, difficulty, deck_amount):
    global running_count
    running_count = check_and_shuffle(running_count)
    
    # define balance and bet
    if difficulty == 3:
        print(f"Your balance is {balance}")
        bet = int(input("How much would you like to bet?\n-"))
    else:
        bet = 0

    user_cards = []
    dealer_cards = []

    # generate an index to use for both arrays
    # generate the value for the computer using said index
    # generate the value for the user using said index
    # remove the value from the computer cards
    # remove the value from the user cards
    # edit the running count

    card_index = random.randint(0, len(computer_cards) - 1) 
    user_card1 = computer_cards[card_index]
    user_cards.append(human_cards[card_index])
    computer_cards.pop(card_index)
    human_cards.pop(card_index)
    running_count += to_count_value(user_card1)

    card_index = random.randint(0, len(computer_cards) - 1)
    user_card2 = computer_cards[card_index]
    user_cards.append(human_cards[card_index])
    computer_cards.pop(card_index)
    human_cards.pop(card_index)
    running_count += to_count_value(user_card2)

    card_index = random.randint(0, len(computer_cards) - 1)
    dealer_card1 = computer_cards[card_index]
    dealer_cards.append(human_cards[card_index])
    computer_cards.pop(dealer_card1)
    human_cards.pop(dealer_card1)
    running_count += to_count_value(dealer_card1)

    card_index = random.randint(0, len(computer_cards) - 1)
    dealer_card2 = computer_cards[card_index]
    dealer_cards.append(human_cards[card_index])
    computer_cards.pop(dealer_card2)
    human_cards.pop(dealer_card2)
    # don't change the count cause the user can't see this card

    # calculate the sums for the user and dealer
    user_sum = user_card1 + user_card2
    dealer_sum = dealer_card1 + dealer_card2

    # let the program know who has aces and how many
    user_aces = 0
    dealer_aces = 0

    if user_card1 == 11:
        user_aces += 1
    if user_card2 == 11:
        user_aces += 1
    if dealer_card1 == 11:
        dealer_aces += 1
    if dealer_card2 == 11:
        dealer_aces += 1

    loop = True
    can_double = True
    or_x2 = " or x2"

    # starting blackjack detection for user
    if user_sum == 21:
        loop = False
        print_cards_real(dealer_cards, user_cards)
        if dealer_sum == 21:
            print("It's a push!")
            return balance
        else:
            print("You got Blackjack!")
            return balance + bet * 1.5
    
    # starting blackjack detection for dealer
    if dealer_sum == 21:
        loop = False
        print_cards_real(dealer_cards, user_cards)
        print(f"\nUnfortunate, the dealer got Blackjack!")
        return balance - bet

    while loop is True:
        print_cards(dealer_cards, user_cards)
        if difficulty <= 2:
            print(f"Running count: {running_count}")
        if difficulty == 1:
            print(f"True count: {running_count / deck_amount}")

        action = input(f"What would you like to do?\nYou can stand or hit{or_x2}\n>").lower()

        # if the player hits
        if action == "hit":
            new_card = computer_cards[random.randint(0, len(computer_cards) - 1)]
            user_sum += new_card
            running_count += to_count_value(new_card)
            card_index = computer_cards.index(new_card)
            user_cards.append(human_cards[card_index])

            human_cards.pop(card_index)
            computer_cards.pop(card_index)

            # makes aces work dw about it
            if new_card == 11:
                user_aces += 1

            if user_sum > 21:
                if user_aces > 0:
                    user_sum -= 10
                    user_aces -= 1
                else:
                    print_cards_real(dealer_cards, user_cards)
                    print("Unfortunate, you bust!")
                    return balance - bet

        # if the player doubles
        elif action == "x2":
            # ensures this can only be done on the first round
            if can_double is True:
                new_card = computer_cards[random.randint(0, len(computer_cards) - 1)]
                user_sum += new_card
                running_count += to_count_value(new_card)
                card_index = computer_cards.index(new_card)
                user_cards.append(human_cards[card_index])

                human_cards.pop(card_index)
                computer_cards.pop(card_index)

                # makes aces work dw about it
                if new_card == 11:
                    user_aces += 1

                if user_sum > 21:
                    if user_aces > 0:
                        user_sum -= 10
                        user_aces -= 1
                    else:
                        print_cards_real(dealer_cards, user_cards)
                        print("Unfortunate, you bust!")
                        return balance - bet

                bet += bet

        elif action == "hint":
            if running_count / deck_amount >= 1:
                print(f"The count is {running_count}, it is getting high so you should bet higher\nRemember the higher the number the higher % of high cards")
            else:
                print(f"The count is {running_count}, it is getting low so you should bet lower\nRemember the lower the number the lower % of high cards")

        # if the player stands
        elif action == "stand":
            print_cards_real(dealer_cards, user_cards)
            running_count += to_count_value(dealer_card2)
            while dealer_sum < 17:
                new_card = computer_cards[random.randint(0, len(computer_cards) - 1)]
                dealer_sum += new_card
                running_count += to_count_value(new_card)
                card_index = computer_cards.index(new_card)
                dealer_cards.append(human_cards[card_index])
                print_cards_real(dealer_cards, user_cards)

                human_cards.pop(card_index)
                computer_cards.pop(card_index)

                # makes aces work dw about it
                if new_card == 11:
                    dealer_aces += 1

                if dealer_sum > 21:
                    if dealer_aces > 0:
                        dealer_sum -= 10
                        dealer_aces -= 1
                    else:
                        print("Awesome, the dealer busts!")
                        return balance + bet

                
            if user_sum == dealer_sum:
                print("Interesting, a push!")
                return balance
            if user_sum < dealer_sum:
                print("Unfortunate, the dealer wins!")
                return balance - bet
            if user_sum > dealer_sum:
                print("Awesome, you win!")
                return balance + bet

            loop = False
        can_double = False
        or_x2 = ""

# main lines of code
print("Hello, welcome to the card counting trainer!\nThis casino reshuffles after ≈50% has been dealt")
print("At any point, type \"hint\" to get a hint")
difficulty = int(input("For easy mode type 1 (you will see the running count and the true count)\nfor normal type 2 (you will see only the running count)\nand for hard type 3 (normal blackjack with no extra help)\n>"))
deck_amount = int(input("How many decks would you like there to be?\n>"))
template_to_cards(deck_amount)

if difficulty == 3:
    balance = int(input("What is your balance?\n>"))
else:
    balance = 1

while balance > 0:
    balance = blackjack(balance, difficulty, deck_amount)

print("You have no more money\nLeave the casino")
