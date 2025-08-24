
def blackjack(user, dealer):
    if user == 21 and dealer == 21:
        print("Both you and the dealer have BlackJack!")
        print("It's a draw!")
        exit()
    elif user == 21:
        print("BlackJack!")
        print("You won!")
        exit()
    elif dealer == 21:
        print("BlackJack!")
        print("You lost!")
        exit()

def above_21(user):
    if user > 21:
        print("You lost! Your total is over 21.")
        exit()

def result(user, dealer):
    if user > 21:
        print("You lost! Your total is over 21.")
        exit()
    elif user == dealer:
        print("It's a draw!")
    elif user > dealer and user <= 21:
        print("You won!")
    elif user < dealer and dealer <= 21:
        print("You lost!")
    elif user < 21 and dealer > 21:
        print("You won! The dealer's total is over 21.")
