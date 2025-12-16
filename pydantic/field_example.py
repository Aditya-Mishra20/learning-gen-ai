from pydantic import BaseModel
from typing import List, Optional, Dict


class Cart(BaseModel):
    id: int
    items: List[str]
    quantity: Dict[str, int]


class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None  #field that can be str or none


cart_data = {
    "id": 1,
    "items": ["Laptop", "Phone", "Tablet"],
    "quantity": {"Laptop": 1, "Phone": 2, "Tablet": 3}
}


cart = Cart(**cart_data)

print(cart)