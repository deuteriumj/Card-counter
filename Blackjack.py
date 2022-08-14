import random

computer_cards_template = [11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8 ,8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
human_cards_template = ["A", "A", "A", "A", 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8 ,8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K"]

deck_amount = 1
difficulty = 0
running_count = 0
true_count = 0

computer_cards = []
human_cards = []

def template_to_cards(deck_amount):
    for i in range(deck_amount):
        computer_cards.extend(computer_cards_template)
        human_cards.extend(human_cards_template)

def print_cards(dealer_cards, user_cards):
    print(f"\nDealer's cards:\n{dealer_cards[0]} _\nYour cards:\n{' '.join(map(str, user_cards))}")

def print_cards_real(dealer_cards, user_cards):
    print(f"\nDealer's cards:\n{' '.join(map(str, dealer_cards))}\nYour cards:\n{' '.join(map(str, user_cards))}")

def blackjack(balance, difficulty):
    # define balance and bet
    if difficulty == 3:
        print(f"Your balance is {balance}")
        bet = int(input("How much would you like to bet?\n-"))
    else:
        bet = 0

    # generate the values for the computer
    user_card1 = computer_cards[random.randint(0, len(computer_cards)) - 1]
    computer_cards.remove(user_card1)
    user_card2 = computer_cards[random.randint(0, len(computer_cards)) - 1]
    computer_cards.remove(user_card2)
    dealer_card1 = computer_cards[random.randint(0, len(computer_cards)) - 1]
    computer_cards.remove(dealer_card1)
    dealer_card2 = computer_cards[random.randint(0, len(computer_cards)) - 1]
    computer_cards.remove(dealer_card2)

    # generate the cards to show the user
    user_cards = [human_cards[computer_cards.index(user_card1)], human_cards[computer_cards.index(user_card2)]]
    dealer_cards = [human_cards[computer_cards.index(dealer_card1)], human_cards[computer_cards.index(dealer_card2)]]

    # remove used cards from decks
    human_cards.remove(user_cards[0])
    human_cards.remove(user_cards[1])
    human_cards.remove(dealer_cards[0])
    human_cards.remove(dealer_cards[1])

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

        action = input(f"What would you like to do?\nYou can stand or hit{or_x2}\n>")

        # if the player hits
        if action == "hit":
            new_card = computer_cards[random.randint(0, len(computer_cards)) - 1]
            user_sum += new_card
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
                new_card = computer_cards[random.randint(0, len(computer_cards)) - 1]
                user_sum += new_card
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

        # if the player stands
        elif action == "stand":
            print_cards_real(dealer_cards, user_cards)
            while dealer_sum < 17:
                new_card = computer_cards[random.randint(0, len(computer_cards)) - 1]
                dealer_sum += new_card
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
def main():
    print("Hello, welcome to the card counting trainer!")
    difficulty = int(input("For easy mode type 1, for medium type 2 and for hard type 3\n>"))
    deck_amount = int(input("How many decks would you like there to be?\n>"))
    template_to_cards(deck_amount)
    input(len(computer_cards))

    if difficulty == 3:
        balance = int(input("What is your balance?\n>"))
    else:
        balance = 1

    while balance > 0:
        balance = blackjack(balance, difficulty)

    print("You have no more money\nLeave the casino")


# run code when code is run
if __name__ == "__main__":
    main()
