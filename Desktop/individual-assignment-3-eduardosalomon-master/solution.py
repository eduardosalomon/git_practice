# -*- coding: utf-8 -*-

class products:

    def __init__(self, product ,price):
        self.product = product
        self.price = price   
    
class tier:
    def __init__(self, name, desc, type_, amount):
        self.name = name
        self.desc = desc
        self.type = type_
        self.amount = amount
        
    def calculate_discount(self, total):
        if self.type == "fixed":
            return self.amount
        elif self.type == "percentual":
            return total * self.amount
        else:
            return 0
        
class shoppingcart:
    
    def __init__(self):
        self.products = []
        self.tier = None
        self.total = 0
        self.disc = 0
        
    def add_product(self, product):
        self.products.append(product)
        
    def calculate_price(self):
        sum = 0
        for item in self.products:
            sum += item.price
            
        return sum
    
    def calculate_price_with_discounts(self):
        self.total = self.calculate_price()
        
        if self.tier:
            self.disc = self.tier.calculate_discount(total)
        return self.total - self.disc
    
    def print_receipt(self):
        total = self.calculate_price_with_discounts()
        
        
        print("--- Cart summary ---")
        print("Sub Total:    $" + str(round(self.total, 2)))
        print("Discount:    $" + str(round(self.disc,2)))
        print("Total:      $" + str(round(total, 2)))
    
        
guitar = products("guitar", 1000)
pick_box = products("pick", 5)
guitar_strings = products("string", 10)

silver = tier("Silver tier", "Provides a fixed 5$ discount in the total price of the ShoppingCart.", "fixed", 5)
gold = tier("Gold tier", "Provides a 10% discount to the total price of the ShoppingCart.", "percentual", 0.1)
    
# Shpping cart
shop = shoppingcart()


# Tier definition
shop.tier = gold

# Products added to the shoppiong cart
shop.add_product(guitar)
shop.add_product(pick_box)
    

# Receipt
shop.print_receipt()




