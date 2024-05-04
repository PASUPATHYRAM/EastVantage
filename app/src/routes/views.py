from fastapi import APIRouter,Depends,Body
from app.src.schemas.addressbook_schema import AddressBookSchema,AddressSchema,AddressResponseSchema
from ..dbsetup.depedenecy import get_db
from typing import Dict,List
from sqlalchemy.orm import Session
from ..service.request_call import make_request
from ..service.logic import add_data_to_db,get_data,convert_schema,get_data_by_id,update_data,del_data_by_id

route=APIRouter(prefix='/v1',tags=['AddressBook'])

@route.post('/address/add',response_model=Dict)
def post_address(request_model:AddressSchema,db:Session=Depends(get_db)):
    address=request_model.address_lines
    name=request_model.name
    phone=request_model.phone
    return add_data_to_db(db,make_request(address),name,phone)

@route.get('/getall',response_model=List[AddressResponseSchema])
def get_address(db:Session=Depends(get_db)):
    return convert_schema(get_data(db))

@route.put('/update/{id}',response_model=Dict)
def update_record(id:int,request_model:AddressSchema= Body(...),db:Session=Depends(get_db)):
    return update_data(db,get_data_by_id(db,id),request_model)


@route.delete('/delete/{id}',response_model=Dict)
def delete_record(id:int,db:Session=Depends(get_db)):
    return del_data_by_id(db,id)



