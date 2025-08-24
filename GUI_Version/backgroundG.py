


from valuesG import card_values, cards, type
import random


class Card:
    card_shown = []  

    @classmethod
    def choosing(cls):
        card_1 = random.choice(cards)
        type_1 = random.choice(type)
        card_2 = random.choice(cards)
        type_2 = random.choice(type)
        value_1 = card_values[card_1]
        value_2 = card_values[card_2]

        card_data = {
            "cards": [(card_1, type_1), (card_2, type_2)],
            "total_value": value_1 + value_2
        }

        cls.card_shown.append(card_data)

        label = f"""
{card_1} {type_1}   {card_2} {type_2}
Total value: {value_1 + value_2}
"""


    @staticmethod
    def take_anther_one(question):
        if question.lower() == 'hit':
            ano_card = random.choice(cards)
            ano_type = random.choice(type)
            ano_value = card_values[ano_card]
            label=f"""
{ano_card} {ano_type}
Value: {ano_value}
"""

            # ⬇️ Update the last drawn card set
            if Card.card_shown:
                Card.card_shown[0]["cards"].append((ano_card, ano_type))
                Card.card_shown[0]["total_value"] += ano_value
                return label
    
    
    @classmethod
    def show_user_cards(cls):
        if cls.card_shown:  # Make sure at least one hand exists
            first_hand = cls.card_shown[0]

            # Join all cards into a single line: "8 Clubs   9 Spades   2 Hearts"
            card_line = "   ".join(
                f"{name} {type_}" for name, type_ in first_hand["cards"])

            total = first_hand["total_value"]
            return f"{card_line}\nTotal value: {total}"
        

    @classmethod
    def show_dealer_cards(cls):
        if cls.card_shown:  # Make sure at least one hand exists
            second_hand = cls.card_shown[1]

            # Join all cards into a single line: "8 Clubs   9 Spades   2 Hearts"
            card_line = "   ".join(
                f"{name} {type_}" for name, type_ in second_hand["cards"])

            total = second_hand["total_value"]
            return f"{card_line}\nTotal value: {total}"


