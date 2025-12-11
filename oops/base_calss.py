class Chai:
    def __init__(self, type_, strength):
        self.type_of_Chai = type_
        self.strength = strength
        

# code duplication example
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level


# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)  #calling base class constructor
#         self.spice_level = spice_level
    

class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)  #calling base class constructor
        self.spice_level = spice_level