class Computer:
    def _init_(self):
        self._maxprice = 900
    def sell(self):
        print("Selling price{}" .format(self.maxprice))
    def setMaxPrice(self, price):
        self._maxprice = price
        
c = Computer()
c.sell()