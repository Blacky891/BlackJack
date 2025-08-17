
# Blackjack Game

A simple console-based Blackjack game implemented in Python.

## How to Play

1. Both you and the dealer are dealt two cards at the start.
2. Your cards are shown, and one of the dealer’s cards is visible.
3. You can choose to:
   - **Hit** — take another card to get closer to 21.
   - **Stand** — keep your current hand and end your turn.
4. The goal is to get as close to 21 points as possible **without going over**.
5. Number cards are worth their face value, face cards (Jack, Queen, King) are worth 10, and Aces can count as 1 or 11.
6. After you stand, the dealer reveals their hidden card and draws cards automatically:
   - Dealer must hit if their total is less than 17.
   - Dealer stands once reaching 17 or more.
7. If either player or dealer goes over 21, they **bust** and lose.
8. If neither busts, the hand with the higher total wins.
9. If both have the same total, it's a **push** (a tie).

