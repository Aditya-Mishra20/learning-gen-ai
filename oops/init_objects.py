class ChaiOrder:
    def __init__(self, type_of_Chai, size):
        self.type_of_Chai = type_of_Chai
        self.size = size
        
    def summary(self):
        return f"Order: {self.size} ml of {self.type_of_Chai} chai."



order1 = ChaiOrder("Masala", 300)
print(order1.summary())
order2 = ChaiOrder("Ginger", 250)   
print(order2.summary())