from Stocks import Stocks
from Trade import Trade

def AddTrade(stock):
    print 'Add trade for ' + stock.symbol
    quantity = raw_input('Please enter the quantity: ')
    buy = raw_input('(B)uy or (S)ell: ')
    buy = buy == 'B'
    price = raw_input('Please enter the trade price: ')
    trade = Trade(quantity, buy, price)
    stock.addTrade(trade)

def StockOptions(stock):
    while True:
        print 'Input DY for dividend yield'
        print 'Input PE for P/E ratio'
        print 'Input ADD to add a trade'
        print 'Input VWSP for volume weighted stock price'
        reply = raw_input('r to return to main menu: ')
                
        if reply == 'r':
            break
        if reply == 'DY':
            marketPrice = raw_input('Please input market price: ')
            print 'Dividend yield ' + str(stock.dividendYield(marketPrice))
        if reply == 'PE':
            marketPrice = raw_input('Please input market price: ')
            print 'PE ratio ' + str(stock.peRatio(marketPrice))
        if reply == 'ADD':
            AddTrade(stock)
        if reply == 'VWSP':
            print stock.vwsp()
            

stocks = Stocks()

while True:
    print 'Stocks:'
    for stock in stocks.stocks:    
        print stock.symbol
    print 'Input a stock name for more options'
    print 'Input GBCE for GBCE All Share Index'
    reply = raw_input('q to Quit: ')
    
    if reply == 'q':
        break
    stock = stocks.get(reply)
    if stock != 0:
        StockOptions(stock)
    if reply == 'GBCE':
        print stocks.geometricMean()

print 'Quit'


