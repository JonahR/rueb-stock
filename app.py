from profile import Profile
from stock import Stock
from graph import Graph
from watchlist import Watchlist


# Methods for each available command
def stockPriceCmd():
    print("Stock price for:", end=" ")
    ticker = input()
    lookedup_stock = Stock(ticker)
    print(lookedup_stock.getPrice())


def watchlistCmd():
    print("1) View watchlist\n2) Add stock to watchlist\n3) Remove stock from watchlist\n")
    print(">", end=" ")
    user_input = input()

    # Displays watchlist
    if user_input == "1":
        if logged_in:
            my_profile.watchlist.printWatchlist()
        else:
            user_watchlist.printWatchlist()

    # Adds a stock to the watchlist
    elif user_input == "2":
        print("Select a ticker:", end=" ")
        ticker = input()
        if logged_in:
            my_profile.watchlist.addToWatchlist(ticker)
        else:
            user_watchlist.addToWatchlist(ticker)
        

    # Removes a stock from the watchlist
    elif user_input == "3":
        print("Select a ticker:", end=" ")
        ticker = input()
        if logged_in:
            my_profile.watchlist.removeFromoWatchlist(ticker)
        else:
            user_watchlist.removeFromWatchlist(ticker)

def portfolioCmd():
    print("1) Portfolio details\n2) Buy stock\n3) Sell stock")
    print(">", end=" ")
    user_input = input()

    if user_input == "1":
        print("Unimplemented")
    elif user_input == "2":
        print("Unimplemented")
    elif user_input == "3":
        print("Unimplemented")


def graphCmd():
    print("Graph stock:", end=" ")
    ticker = input()
    g = Graph(ticker)
    g.start()


def createAccount():
    username = input("What would you like your username to be: ")
    username_list = []

    with open("database/usernames.txt", "r") as f:
        for username_on_line in f:
            username_list.append(username_on_line.strip())
    f.close()

    if username not in username_list:
        with open("database/usernames.txt", "a+") as f:
            f.write(username + "\n")
        f.close()
        with open("database/" + username + ".txt", "a+") as f:
            f.write("")
        f.close()
        print("You created an account with the username: " + username)
    else:
        print("Sorry, that username has been taken.")


# If the user enters the correct username it will create a global my_profile var
def login():
    username = input("Enter your username: ")
    username_list = []

    with open("database/usernames.txt", "r") as f:
        for username_on_line in f:
            username_list.append(username_on_line.strip())
    f.close()

    if username in username_list:
        global  my_profile
        global logged_in

        my_profile = Profile(username)
        logged_in = True
        print("You have logged into " + username)
    else:
        print("That account does not exist.")

# Exits application
# Changes global variable running
# Potentially add code for saving/backing up data here
def exit():
    global running, logged_in
    running = False
    if logged_in:
        my_profile.save()
        print("working")
    print("Goodbye")


# starts application and creates loop until exit command
def start():
    global running, logged_in
    logged_in = False
    running = True

    print("\n\n\nWelcome to the Rueb Stock Trader\nType the corresponding number to do a command or type 'exit' to exit")

    while running:
        print("\n1) Look up price\n2) Watchlist options\n5) Login\n6) Create Account")
        print(">", end=" ")
        user_input = input()

        # Look up price
        if user_input == "1":
            stockPriceCmd()

        # watch list
        elif user_input == "2":
            watchlistCmd()

        # portfolio
        elif user_input == "3":
            portfolioCmd()

        # graph
        elif user_input == "4":
            graphCmd()

        # login
        elif user_input == "5":
            login()

        # create account
        elif user_input == "6":
            createAccount()

        # exit
        elif user_input == "exit":
            exit()

        # bad input
        else:
            print("That is an invalid command.")


# This will be edited when profiles are included.
user_watchlist = Watchlist()
# start application
start()
