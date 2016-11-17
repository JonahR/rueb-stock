from stock import Stock

running = True;

print("Welcome to the Rueb Stock Trader\nType the corresponding number to do a command or type 'exit' to exit")

while(running):
    print("\n1) Look up price\n2)Watchlist options")
    print(">", end=" ")
    user_input = input()
    
    #Look up price
    if(user_input == "1"):
        print("Stock price for:", end=" ")
        ticker = input()
        lookedup_stock = Stock(ticker)
        print(lookedup_stock.getPrice())
    
    #watch list
    elif(user_input == "2"):
        print("1) View watchlist\n2) Add stock to watchlist\n3) Remove stock remove watchlist")
        print(">", end=" ")
        user_input = input()
        
        if(user_input == "1"):
            print("Unimplemented")
        elif(user_input == "2"):
            print("Unimplemented")
        elif(user_input == "3"):
            print("Unimplemented")
    
    #exit
    elif(user_input == "exit"):
        running = False;
        print("Goodbye")
   
   #bad input
    else:
        print("That is an invalid command.")
        
        