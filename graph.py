import matplotlib.pyplot as plt
from stock import Stock

#Grapher
class Graph:
    
    #creates stock object with ticker variable
    def __init__(self, ticker):
        self.stock = Stock(ticker)
    
    #updates price and returns value
    def start(self):
        plt.axis([0, 10, 0, 1])
        plt.ion()

        arr = []
        for i in range(100):

            min = 10000
            max = 0
            curr = float(self.stock.getPrice())
            if(curr < min):
                min = curr
            if(curr > max):
                max = curr
            plt.axis([0, i+1, min-1, max+1])
            arr.append(curr)
            plt.plot(arr)
            plt.pause(1)

        while True:
            plt.pause(0.05)
    
    
    


