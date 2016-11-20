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
	# Displays the prices of all tickers in watchlist
	def displayWatchlist(self):
		for ticker in self.watchlist:
			lookedup_stock = Stock(ticker)
			print(ticker + ":" + lookedup_stock.getPrice())
	# Removes a ticker from the watchlist given the proper name
	def removeFromWatchlist(self):
		ticker = self.getTicker()
		self.watchlist.remove(ticker)


