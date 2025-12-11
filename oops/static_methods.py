class  ChaiUtils:
    @staticmethod #decorator is used to define static method    
    def chai_ingredients(text):
        return [item.strip() for item in text.split(",")]



raw = "Tea leaves, Milk, Sugar, Ginger, Cardamom, Cloves"

obj = ChaiUtils().chai_ingredients(raw) 
print(obj)