class Tealeaf:
    def __init__(self, quality):
        self._quality = quality  #private attribute
        
    @property #this is used to get value of private attribute
    def quality(self):
        return self._quality +2
    
    @quality.setter #this is used to set value to private attribute
    def quality(self, value):
        if 1 <= value <= 10:
            self._quality = value
        else: 
            raise ValueError("Quality must be between 1 and 10") 
        
        
leaf = Tealeaf(5)
print(leaf.quality)  #accessing private attribute using getter