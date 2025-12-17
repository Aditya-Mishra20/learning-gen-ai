from typing import List, Optional
from pydantic import BaseModel



class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address : Address


address = Address(
    street="123 something",
    city= "Jaipur",
    postal_code="12345"
)

user_data = {
    "id":123,
    "name":"Adi",
    "address":address
}



user = User(**user_data)
    

print(user)
