from typing import Optional
from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    name: str = Field(
        ..., #required field
        min_length=3,
        max_length=50,
        description="The name of the employee"
        example="John Doe"
    )
    age: int = Field(
        ge=0,
        le=100,
        description="The age of the employee",
        example=30,
    )
    email: str = Field(
        ...,
        regex=r''


    )
    phone: Optional[str] = None
    department: str
    salary: float = Field(
        ...,
        ge = 10000,
        le = 100000,
        description="The salary of the employee"
        example=50000
    )
    is_active: bool = True
    discount: float = Field(
        default=0,
        ge=0,
        le=100,
        description="The discount of the employee"
        example=100
    )





