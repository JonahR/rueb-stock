from stock import Stock

running = True;

print("Welcome to the Rueb Stock Trader\nType the corresponding number to do a command or type 'exit' to exit")

while(running):
    print("\n1) Look up price\n2)View watchlist")
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
        print("Watchlist")
    
    #exit
    elif(user_input == "exit"):
        running = False;
        print("Goodbye")
   
   #bad input
    else:
        print("That is an invalid command.")
        
        