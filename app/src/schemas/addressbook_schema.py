from pydantic import BaseModel,Field,field_validator


#requestmodel
class AddressSchema(BaseModel):
    name:str
    address_lines:str
    phone:int

#responsemodel
class AddressBookSchema(BaseModel):
    details: AddressSchema
    lat:float = Field(..., ge=-90, le=90)
    long: float = Field(..., ge=-180, le=180)
    city: str
    state: str
    zipcode: str
    country: str

class AddressResponseSchema(AddressBookSchema):
    id: int
    class Config:
        orm_mode=True





