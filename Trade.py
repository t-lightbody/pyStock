from datetime import datetime

class Trade:
    def __init__(self, quantity, buy, price):
        self.timestamp = datetime.now()
        self.quantity = quantity
        self.buy = buy
        self.price = price
        self.next = 0
