import urllib.request
import json


# Stock object
class Stock:

    # creates stock object with ticker variable
    def __init__(self, ticker):
        self.ticker = ticker
   
    # updates price and returns value
    def getPrice(self):
        if self.update() is not False:
            return self.price
    
    # determines if a stock exists        
    def exists(self):
        try:
            u = urllib.request.urlopen("http://finance.google.com/finance/info?client=ig&q=NSE:" + self.ticker)
            return True
        except Exception as error:
            return False
        
    # calls API to update values
    def update(self):
        try:
            url = "http://finance.google.com/finance/info?client=ig&q=NSE:" + self.ticker
            u = urllib.request.urlopen(url)
            content = u.read()
            data = json.loads(content[3:].decode())
            info = data[0]

            # update price and time
            self.price = str(info["l"])
            self.time = str(info["ltt"])
        except Exception as error:
            print("You tried to update a stock that does not exist. Consider using the exists function")