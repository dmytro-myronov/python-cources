from pydantic import BaseModel
from typing import List

class AddressCreate(BaseModel):
    street: str
    city: str

class AddressRead(AddressCreate):
    id: int
    class Config:
        orm_mode = True

class CustomerCreate(BaseModel):
    name: str
    email: str

class CustomerRead(CustomerCreate):
    id: int
    addresses: List[AddressRead] = []
    class Config:
        orm_mode = True
