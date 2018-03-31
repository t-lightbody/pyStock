from datetime import datetime, timedelta

class Stock:
    def __init__(self, symbol, lastDividend, parValue):
        self.symbol = symbol
        self.lastDividend = lastDividend
        self.parValue = parValue
        self.lastTrade = 0

    def dividendYield(self, marketPrice):
        marketPrice = float(marketPrice)
        if marketPrice > 0:
            return self.lastDividend / marketPrice
        else:
            return 'Undefined'

    def peRatio(self, marketPrice):
        marketPrice = float(marketPrice)
        dividend = self.dividendYield(marketPrice)
        if dividend > 0:
            return marketPrice / dividend
        return 'Undefined'

    def addTrade(self, trade):
        if self.lastTrade != 0:
            trade.next = self.lastTrade
        self.lastTrade = trade

    def recentTrades(self):
        recentPeriod = datetime.now() - timedelta(minutes=15)
        nextTrade = self.lastTrade
        trades = []
        while nextTrade != 0 and nextTrade.timestamp > recentPeriod:
            trades.append(nextTrade)
            if nextTrade.next != 0:
                nextTrade = nextTrade.next
            else:
                break
        return trades

    def vwsp(self):
        trades = self.recentTrades()
        sumTpByQuantity = 0
        sumQuantity = 0
        for trade in trades:
            sumTpByQuantity += int(trade.price) * int(trade.quantity)
            sumQuantity += int(trade.quantity)
        if sumQuantity == 0:
            return 0
        return sumTpByQuantity / sumQuantity
            
