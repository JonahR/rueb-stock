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
        self.watchlist.append(ticker)

    # Returns a dictionary of ticker and their values
    def getWatchlist(self):
            priceWatchlist = {}
            for ticker in self.watchlist:
                lookedup_stock = Stock(ticker)
                priceWatchlist[ticker] = lookedup_stock.getPrice()
            return priceWatchlist

    # Removes a ticker from the watchlist given the proper name
    def removeFromWatchlist(self):
        ticker = self.getTicker()
        self.watchlist.remove(ticker)
