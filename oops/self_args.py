class Chaicup:
    size = 42 # ml
    
    def describe(self):
        return f"This chaicup holds {self.size} ml of chai."
    
    
chaicup = Chaicup()
print(chaicup.describe())
print(Chaicup.describe(chaicup))
cup = Chaicup()
cup.size = 250
print(cup.describe())