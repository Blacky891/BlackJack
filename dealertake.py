

import random
def dealer_take():
    from background import Card
    from values import card_values, cards, type
    import time
    import os
    if Card.card_shown[1]["total_value"] >= 17:
        print("The dealer has enough value, no more cards taken.\n")
        return
    else:
        while Card.card_shown[1]["total_value"] < 17:
            time.sleep(1)
            print("The dealer is taking another card")
            for _ in range(3): 
                print(".", end="", flush=True)
                time.sleep(1)
            print()

            ano_card = random.choice(cards)
            ano_type = random.choice(type)
            another_value = card_values[ano_card]
            print("The dealer has taken another card: ")
            if Card.card_shown:
                Card.card_shown[1]["cards"].append((ano_card, ano_type))
                Card.card_shown[1]["total_value"] += another_value
            time.sleep(1)
            print(f"""
{ano_card} {ano_type}
Value: {another_value}
""")
            time.sleep(1)
            print(f"The dealer's total value is now: {Card.card_shown[1]["total_value"]}\n")
            time.sleep(1.5)

    
    return another_value
