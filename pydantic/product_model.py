from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    price:float
    in_stock:bool = True


product_one = Product(id=1, name="Laptop", price=1000.0, in_stock=True)

product_two = Product(id=2, name="Phone", price=500.0)


product_three = Product(id=3, name="Tablet", price=300.0)



