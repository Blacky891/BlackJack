

from background import Card
from dealertake import dealer_take
from wincondit import result, blackjack, above_21
import time
import os

Card.choosing()

Card.choosing()

blackjack(Card.card_shown[0]["total_value"], Card.card_shown[1]["total_value"])

question = "hit"
while question != 'stand' and Card.card_shown[0]["total_value"] < 21:
    question = input('Hit or stand ? ').lower()
    if question == 'hit':
        Card.take_anther_one(question)
        os.system("cls" if os.name == "nt" else "clear")
        Card.show_cards()
        above_21(Card.card_shown[0]["total_value"])
        blackjack(Card.card_shown[0]["total_value"], Card.card_shown[1]["total_value"])
        time.sleep(3)
os.system("cls" if os.name == "nt" else "clear")

dealer_take()

Card.show_cards()

blackjack(Card.card_shown[0]["total_value"], Card.card_shown[1]["total_value"])
result(Card.card_shown[0]["total_value"], Card.card_shown[1]["total_value"])
