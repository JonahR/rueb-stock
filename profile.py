from watchlist import Watchlist


class Profile:

    def __init__(self, username):
        self.watchlist = Watchlist()
        with open("database/" + username + ".txt", "r") as f:
            for stock_on_line in f:
                self.watchlist.addToWatchlist(stock_on_line.strip())




