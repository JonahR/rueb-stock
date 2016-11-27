from stock import Stock


# Watchlist
class Watchlist:

    def __init__(self):
        self.watchlist = []

    # Returns a ticker the user imputs
    def getTicker(self):
        print("Select a ticker:", end=" ")
        ticker = input()
        return ticker

    # Adds a ticker to the watchlist
    def addToWatchlist(self):
        ticker = self.getTicker()
        s = Stock(ticker)
        if(s.exists()):
            self.watchlist.append(s)
        else:
            print("This stock does not exist")

    # Returns a dictionary of ticker and their values
    def getWatchlist(self):
        return self.watchlist

    # Removes a ticker from the watchlist given the proper name
    def removeFromWatchlist(self):
        ticker = self.getTicker()
        
        for s in self.watchlist:
            if(s.ticker == ticker):
                self.watchlist.remove(s)

    # Returns watchlist in nicely formated string
    def printWatchlist(self):
        
        # If watchlist is empty it will return False
        if self.watchlist: 
            for s in self.watchlist:
                print(s.ticker + " - " + s.getPrice())
        else:
            print("You have not created a watchlist.")
