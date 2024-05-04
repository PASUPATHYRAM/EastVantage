from app.src.dbsetup.dbsetup import Base
from sqlalchemy import Column,String,Integer,Float


class AddressBookModel(Base):
    __tablename__='addressbook'
    id=Column(Integer,autoincrement=True,primary_key=True)
    name=Column(String)
    lat=Column(Float)
    long=Column(Float)
    address_line=Column(String)
    city=Column(String)
    state=Column(String)
    zipcode=Column(String)
    country=Column(String)
    phone=Column(Integer)


