class Chai:
    def __init__(self, type_):
        self.type = type_
        
    def prepare(self):
        print(f'Preparing a cup of {self.type} chai.')




class MasalaChai(Chai):
    def add_spices(self):
        print('Adding masala spices to the chai.')  
        
        
        
cup = MasalaChai("Masala") #object
cup.prepare()


#composition
class ChaiShop:
    chai_cls = Chai #only to access methods of base class
    def __init__(self):
        self.chai = self.chai_cls("Regular")
    
    def serve(self):
        print(f'Serving a cup of {self.chai.type} chai.')
        self.chai.prepare()
        

order = ChaiShop()
cup = Chai("Masala")
order.serve()
