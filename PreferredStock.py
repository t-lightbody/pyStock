from Stock import Stock

class PreferredStock(Stock):
    def __init__(self, symbol, lastDividend, parValue, fixedDividend):
        self.fixedDividend = fixedDividend
        Stock.__init__(self, symbol, lastDividend, parValue)

    def dividendYield(self, marketPrice):
        return self.fixedDividend * self.parValue / float(marketPrice)
