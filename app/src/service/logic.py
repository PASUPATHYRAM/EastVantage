from sqlalchemy.orm import Session
from typing import Dict
from ..models.addressbook_models import AddressBookModel
from fastapi import HTTPException
from ..logger.loggs import Loggercheck
logger = Loggercheck()


def add_data_to_db(db: Session, address: Dict, name, phone):
    data_model = AddressBookModel(
        name= name,
        lat= address['lat'],
        long= address['long'],
        city= address['city'],
        state= address['state'],
        zipcode= address['zipcode'],
        country= address['country'],
        address_line= address['address'],
        phone= phone

    )
    try:
        db.add(data_model)
        db.commit()
        db.refresh(data_model)
    except Exception as e:
        db.rollback()
        logger.logg_check(f"An error occurred while adding data to the database: {e}")
        raise HTTPException(status_code=404, detail="Details not found")
    logger.logg_check({"message": "Data added successfully"})
    return {"data":"Added Succesfully"}

def convert_schema(data):
    l=[]
    for rec in data:
        l.append({'id':rec.id,
                  'details':{'name':rec.name,'address_lines':rec.address_line,'phone':rec.phone},
                 'lat':rec.lat,
                  'long':rec.long,
                  'city':rec.city,
                  'state':rec.state,
                  'zipcode':rec.zipcode,
                  'country':rec.country
                  })
    return l
def get_data(db:Session):
    data=db.query(AddressBookModel).all()
    if not data:
        logger.logg_check("data not found")
        raise HTTPException(status_code=404, detail="Data not found")
    return data

def get_data_by_id(db:Session,id):
    data=db.query(AddressBookModel).filter(AddressBookModel.id == id).first()
    return data

def update_data(db:Session,data,request_model):
    if not data:
        logger.logg_check("data not found")
        raise HTTPException(status_code=404, detail="Details not found")
    if request_model.address_lines is not None:
        data.address_lines = request_model.address_lines
    if request_model.name is not None:
        data.name = request_model.name
    if request_model.phone is not None:
        data.phone = request_model.phone
    db.add(data)
    db.commit()
    db.refresh(data)
    logger.logg_check({"message": "Data modified successfully"})
    return {"message":"Data modified successfully"}


def del_data_by_id(db: Session, id: int):
    data = db.query(AddressBookModel).filter(AddressBookModel.id == id).first()
    if not data:
        logger.logg_check("Id not found")
        raise HTTPException(status_code=404, detail="Id not found")
    db.delete(data)
    db.commit()
    logger.logg_check({"message": "Data deleted successfully"})
    return {"message": "Data deleted successfully"}






