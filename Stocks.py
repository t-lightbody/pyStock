from Stock import Stock
from PreferredStock import PreferredStock

class Stocks:
    def __init__(self):
        tea = Stock("TEA", 0, 100)
        pop = Stock("POP", 8, 100)
        ale = Stock("ALE", 23, 60)
        joe = Stock("JOE", 13, 250)
        gin = PreferredStock("GIN", 8, 100, 0.2)
        self.stocks = [tea, pop, ale, joe, gin]
        
    
    def get(self, symbol):
        for stock in self.stocks:
            if stock.symbol == symbol:
                return stock
        return 0

    def geometricMean(self):
        n = len(self.stocks)
        product = 1
        for stock in self.stocks:
            vwsp = stock.vwsp()
            if vwsp != 0:
                product = product * vwsp
            else:
                n -= 1
        return product**(1.0/n)
