


from values import card_values, cards, type
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

        print(f"""
{card_1} {type_1}   {card_2} {type_2}
Total value: {value_1 + value_2}
""")

        return card_data["total_value"]

    @staticmethod
    def take_anther_one(question):
        if question.lower() == 'hit':
            ano_card = random.choice(cards)
            ano_type = random.choice(type)
            ano_value = card_values[ano_card]
            print(f"""
{ano_card} {ano_type}
Value: {ano_value}
""")

            # ⬇️ Update the last drawn card set
            if Card.card_shown:
                Card.card_shown[0]["cards"].append((ano_card, ano_type))
                Card.card_shown[0]["total_value"] += ano_value
                return ano_value
    
    
    @classmethod
    def show_cards(cls):
        for hand in Card.card_shown:
            card_line = "   ".join(
            f"{value} {suit}" for value, suit in hand["cards"])
            print(card_line)
            print(f"Total value: {hand['total_value']}\n")
