from stock import Stock

class Portfolio:

    # creates stock object with ticker variable
    def __init__(self, intitalCash):
        self.cash = intitalCash
        self.stocks = {}
    
    def buyStock(self, ticker, quanity):
        s = Stock(ticker)
        if(s.exists()):
            if self.cash - quanity * float(s.getPrice()) >= 0:
                self.cash -= quanity * float(s.getPrice())
                if ticker in self.stocks:
                    self.stocks[ticker] += quanity
                else:
                    self.stocks[ticker] = quanity
            else:
                print("You have insufficent funds for this trade")
        
    def sellStock(self, ticker, quanity):
        s = Stock(ticker)
        
        if self.stocks[ticker] - quanity >= 0:
            self.cash += quanity * float(s.getPrice())
            self.stocks[ticker] -= quanity
        else:
            print("You do not have enough stock for this trade")