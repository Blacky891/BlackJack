

import customtkinter
from backgroundG import Card


app = customtkinter.CTk()
app.title("my app")
app.geometry("1000x700")
app.title("Blackjack")
app.configure(fg_color="#fafafa")

def welcome_game():
    label = customtkinter.CTkLabel(app, text="Welcome to Blackjack!", font=("Arial", 24))
    label.place(relx=0.5, rely=0.1, anchor="center")
    button.place_forget() 
    label.after(3000, label.place_forget)
    label.after(3000, start_game)  

def start_game():
    label = customtkinter.CTkLabel(app, text="Let's start the game!", font=("Arial", 24))
    label.place(relx=0.5, rely=0.1, anchor="center")
    Card.choosing()
    Card.choosing()
    show_user()
    show_dealer()
    button2 = customtkinter.CTkButton(
        app, text="Hit", command=hit, width=60, height=60)
    button2.place(relx=0.4, rely=0.8, anchor="center")
    button3 = customtkinter.CTkButton(
        app, text="Stand", command=stand, width=60, height=60)
    button3.place(relx=0.6, rely=0.8, anchor="center")



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

def hit():
    label = Card.take_anther_one("hit")
    if label:
        hit_label = customtkinter.CTkLabel(app, text=label, font=("Arial", 18))
        hit_label.place(relx=0.5, rely=0.7, anchor="center")
        hit_label.after(2500, hit_label.place_forget)
        show_user()

def stand():
    from dealertakeG import dealer_take
    label = dealer_take()
    if label:
        dealer_label = customtkinter.CTkLabel(app, text=label, font=("Arial", 18))
        dealer_label.place(relx=0.5, rely=0.7, anchor="center")
        dealer_label.after(2500, dealer_label.place_forget)
        show_dealer()

        

button = customtkinter.CTkButton(
    app, text="Start the game", command=welcome_game,
    width=120, height=40)
button.place(relx=0.5, rely=0.5, anchor="center")




app.mainloop()
