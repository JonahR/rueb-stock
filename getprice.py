import urllib.request
import json


def getPrice(ticker):
    url = "http://finance.google.com/finance/info?client=ig&q=NSE:" + ticker
    u = urllib.request.urlopen(url)
    content = u.read()
    data = json.loads(content[3:].decode())
    info = data[0]
    price = str(info["l"])
    time = str(info["ltt"])
    return [price, time]

def printPrice(tickerData):
    print("The currect price is: " + tickerData[0] +
    '\n' + tickerData[1])

print("Stock price for:", end=" ")
ticker = input()
tickerData = getPrice(ticker)
printPrice(tickerData)




