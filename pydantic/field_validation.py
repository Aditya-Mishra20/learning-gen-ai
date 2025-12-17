from pydantic import BaseModel, field_validator, model_validator



class User(BaseModel):
    name: str
    age: int
    
    @field_validator('name')
    def validate_name(cls, v):
        if len(v)<3:
            raise ValueError("Name must be at least 3 characters long")
        return v


class SignUp_Data(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def password_match(cls, v):
        if v.password != v.confirm_password:
            raise ValueError("Passwords do not match")
        return v   #necessary to return the instance of the class

