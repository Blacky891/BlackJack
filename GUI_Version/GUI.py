

import customtkinter
from backgroundG import Card
from winconditG import blackjack, above_21, result

global hit_button
global stand_button

app = customtkinter.CTk()
app.title("my app")
app.geometry("1000x700")
app.title("Blackjack")
app.configure(fg_color="#ffffff")

def welcome_game():
    label = customtkinter.CTkLabel(app, text="Welcome to Blackjack!", font=("Arial", 24))
    label.place(relx=0.5, rely=0.1, anchor="center")
    button.place_forget() 
    label.after(3000, label.place_forget)
    label.after(3000, start_game)  

def start_game():
    global hit_button, stand_button
    label = customtkinter.CTkLabel(app, text="Let's start the game!", font=("Arial", 24))
    label.place(relx=0.5, rely=0.1, anchor="center")
    Card.choosing()
    Card.choosing()
    show_user()
    show_dealer()
    hit_button = customtkinter.CTkButton(
        app, text="Hit", command=hit, width=60, height=60)
    hit_button.place(relx=0.4, rely=0.8, anchor="center")
    stand_button = customtkinter.CTkButton(
        app, text="Stand", command=stand, width=60, height=60)
    stand_button.place(relx=0.6, rely=0.8, anchor="center")
    blackjack_verify()
    if blackjack_verify() == "Both you and the dealer have BlackJack!\nIt's a draw!" or blackjack_verify() == "BlackJack!\nYou won!" or blackjack_verify() == "BlackJack!\nYou lost!":
        hit_button.configure(state="disabled")
        stand_button.configure(state="disabled")




def show_user():
    card_label = Card.show_user_cards()
    user_label = customtkinter.CTkLabel(app, text="Your cards:", font=("Arial", 18))
    user_label.place(relx=0.3, rely=0.3, anchor="center")
    frame = customtkinter.CTkFrame(app, width=300, height=200, corner_radius=15)
    frame.place(relx=0.3, rely=0.5, anchor="center")
    label = customtkinter.CTkLabel(app)
    label.configure(text=card_label)
    label.place(relx=0.3, rely=0.5, anchor="center")

def show_dealer():
    card_label = Card.show_dealer_cards()
    dealer_label = customtkinter.CTkLabel(app, text="Dealer's cards:", font=("Arial", 18))
    dealer_label.place(relx=0.7, rely=0.3, anchor="center")
    frame = customtkinter.CTkFrame(app, width=300, height=200, corner_radius=15)
    frame.place(relx=0.7, rely=0.5, anchor="center")
    label = customtkinter.CTkLabel(app)
    label.configure(text=card_label)
    label.place(relx=0.7, rely=0.5, anchor="center")


# Create the label once (outside of the hit() function)
hit_label = customtkinter.CTkLabel(app, text="", font=("Arial", 18))
hit_label.place(relx=0.5, rely=0.7, anchor="center")
hit_label.place_forget()  # Hide it initially


def hit():
    global hit_button
    label = Card.take_anther_one("hit")
    if label:
        hit_button.configure(state="disabled")  # Disable the button

        hit_label.configure(text=label)
        hit_label.place(relx=0.5, rely=0.7, anchor="center")

        def reset():
            hit_label.place_forget()
            hit_button.configure(state="normal")  # Re-enable button

        # After 2.5s, hide label and re-enable button
        if above_21_verify() != "stop":
            hit_label.after(2500, reset)
        show_user()
        above_21_verify()
        blackjack_verify()


def stand():
    from dealertakeG import dealer_take
    label = dealer_take()

    if label:
        # Disable the stand button
        stand_button.configure(state="disabled")
        hit_button.configure(state="disabled")

        dealer_label = customtkinter.CTkLabel(
            app, text=label, font=("Arial", 18))
        dealer_label.place(relx=0.5, rely=0.7, anchor="center")

        dealer_label.after(2500, dealer_label.place_forget)

        show_dealer()
        result_verify()

def blackjack_verify():
    user = Card.card_shown[0]["total_value"]
    dealer = Card.card_shown[1]["total_value"]
    message = blackjack(user, dealer)
    if message:
        result_label = customtkinter.CTkLabel(app, text=message, font=("Arial", 18))
        result_label.place(relx=0.5, rely=0.9, anchor="center")
    return message

def above_21_verify():

    user = Card.card_shown[0]["total_value"]
    message = above_21(user)
    if above_21(user) == "You lost! Your total is over 21.":
        hit_button.configure(state="disabled")
        stand_button.configure(state="disabled")
    if message:
        result_label = customtkinter.CTkLabel(app, text=message, font=("Arial", 18))
        result_label.place(relx=0.5, rely=0.9, anchor="center")
    return "stop"

def result_verify():
    user = Card.card_shown[0]["total_value"]
    dealer = Card.card_shown[1]["total_value"]
    message = result(user, dealer)
    if message:
        result_label = customtkinter.CTkLabel(app, text=message, font=("Arial", 18))
        result_label.place(relx=0.5, rely=0.9, anchor="center")

        

button = customtkinter.CTkButton(
    app, text="Start the game", command=welcome_game,
    width=120, height=40)
button.place(relx=0.5, rely=0.5, anchor="center")




app.mainloop()
