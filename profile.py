from watchlist import Watchlist


class Profile:

    def __init__(self, username):
        self.username = username
        self.watchlist = Watchlist()
        with open("database/" + username + ".txt", "r") as f:
            for stock_on_line in f:
                self.watchlist.addToWatchlist(stock_on_line.strip())
        f.close()

    def save(self):
        f = open("database/" + self.username + ".txt", "w")
        data = ""
        for stock in self.watchlist.watchlist:
            data += stock.ticker + "\n"
        f.write(data)
        f.close()

