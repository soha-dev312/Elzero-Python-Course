class Product:
    def __init__(self, price):
        self._price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print("Price must be positive")
p = Product(100)
print(p.price)
p.price = 150
print(p.price)

print("#" * 50)

class Item:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount
    @property
    def final_price(self):
        return self.price - self.discount
item1 = Item("Laptop", 10000, 1500)
print(item1.final_price)
        
        