
from backgroundG import Card


def blackjack(user, dealer):
    if user == 21 and dealer == 21:
        return "Both you and the dealer have BlackJack!\nIt's a draw!"
    elif user == 21:
        return "BlackJack!\nYou won!"
    elif dealer == 21:
        return "BlackJack!\nYou lost!"


def above_21(user):
    if user > 21:
        return "You lost! Your total is over 21."


def result(user, dealer):
    if user > 21:
        return "You lost! Your total is over 21."
    elif user == 21:
        return "BlackJack!\nYou won!"
    elif user == dealer:
        return "It's a draw!"
    elif user > dealer and user <= 21:
        return "You won!"
    elif dealer == 21:
        return "BlackJack!\nYou lost!"
    elif user < dealer and dealer < 21:
        return "You lost!"
    elif user < 21 and dealer > 21:
        return "You won! The dealer's total is over 21."
