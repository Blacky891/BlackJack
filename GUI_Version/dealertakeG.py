import random


def dealer_take():
    from backgroundG import Card
    from valuesG import card_values, cards, type

    label = ""

    if Card.card_shown[1]["total_value"] >= 17:
        return "Dealer has enough cards."

    while Card.card_shown[1]["total_value"] < 17:
        ano_card = random.choice(cards)
        ano_type = random.choice(type)
        another_value = card_values[ano_card]

        if Card.card_shown:
            Card.card_shown[1]["cards"].append((ano_card, ano_type))
            Card.card_shown[1]["total_value"] += another_value

        label += f"{ano_card} {ano_type}\nValue: {another_value}\n\n"

    return label
