import random

computer_cards_template = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8 ,8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
human_cards_template = ["A", "A", "A", "A", 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8 ,8, 8, 8, 9, 9, 9, 9, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K"]

deck_amount = 1

computer_cards = []
human_cards = []

def template_to_cards():
    for i in range(deck_amount):
        computer_cards.append(computer_cards_template)
        human_cards.append(human_cards_template)

def blackjack(balance):
    # define balance and bet
    print(f"Your balance is {balance}")
    bet = int(input("How much would you like to bet?\n-"))

    # generate the values for the computer
    user_card1 = random.randint(1, 13)
    user_card2 = random.randint(1, 13)
    dealer_card1 = random.randint(1, 13)
    dealer_card2 = random.randint(1, 13)

    # generate the cards to show the user
    user_cards = f"{into_card(user_card1)} {into_card(user_card2)}"
    dealer_cards = f"{into_card(dealer_card1)} {into_card(dealer_card2)}"

    user_sum = to_real_value(user_card1) + to_real_value(user_card2)
    dealer_sum = to_real_value(dealer_card1) + to_real_value(dealer_card2)

    # let the program know who has aces and how many
    user_aces = 0
    dealer_aces = 0

    if user_card1 == 1:
        user_aces += 1
    if user_card2 == 1:
        user_aces += 1
    if dealer_card1 == 1:
        dealer_aces += 1
    if dealer_card2 == 1:
        dealer_aces += 1

    loop = True
    can_double = True
    or_x2 = " or x2"
    bust = False

    #  starting blackjack detection for user
    if user_sum == 21:
        loop = False
        if dealer_sum == 21:
            print("It's a push!")
        else:
            print("You got Blackjack!")
            balance += bet * 1.5
    
    # starting blackjack detection for dealer
    if dealer_sum == 21:
        loop = False
        print(f"\nDealer's cards:\n{dealer_cards}\nUnfortunate, the dealer got Blackjack!")
        balance -= bet

    while loop is True:
        print(f"\nDealer's cards:\n{into_card(dealer_card1)} _\nYour cards:\n{user_cards}")

        action = input(f"What would you like to do?\nYou can stand or hit{or_x2}\n-")

        # if the player hits
        if action == "hit":
            new_card = random.randint(1, 13)
            user_sum += to_real_value(new_card)
            user_cards += f" {into_card(new_card)}"

            # makes aces work dw about it
            if new_card == 1:
                user_aces += 1

            if user_sum > 21:
                if user_aces > 0:
                    user_sum -= 10
                    user_aces -= 1
                else:
                    loop = False

        # if the player doubles
        elif action == "x2":
            # ensures this can only be done on the first round
            if can_double is True:
                new_card = random.randint(1, 13)
                user_sum += to_real_value(new_card)
                user_cards += f" {into_card(new_card)}"

                # makes aces work dw about it
                if new_card == 1:
                    user_aces += 1

                if user_sum > 21:
                    if user_aces > 0:
                        user_sum -= 10
                        user_aces -= 1
                    else:
                        loop = False


                bet += bet

                loop = False

        # if the player stands
        elif action == "stand":
            print(f"\nDealer's cards:\n{dealer_cards}")
            while dealer_sum < 17 and not bust:
                new_card = random.randint(1, 13)
                dealer_sum += to_real_value(new_card)

                # makes aces work dw about it
                if new_card == 1:
                    dealer_aces += 1

                if dealer_sum > 21:
                    if dealer_aces > 0:
                        dealer_sum -= 10
                        dealer_aces -= 1
                    else:
                        bust = True
                        dealer_sum = 0

                dealer_cards += f" {into_card(new_card)}"
                print(f"Dealer's cards:\n{dealer_cards}")

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
    balance = int(input("What is your balance?\n-"))
    while balance > 0:
        balance = blackjack(balance)
    print("You have no more money\nLeave the casino")


# run code when code is run
if __name__ == "__main__":
    main()
