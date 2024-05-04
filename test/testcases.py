import unittest
from fastapi.testclient import TestClient
from app.main import get_application
from app.src.dbsetup.depedenecy import get_db
from app.src.models.addressbook_models import AddressBookModel
client=TestClient(get_application())

class TestPostAddress(unittest.TestCase):

    def setUp(self):
        db = next(get_db())
        db.query(AddressBookModel).filter(AddressBookModel.id == 2).delete()
        db.commit()
        db.add(AddressBookModel(id=2, name="John Doe", phone="1234567890",
                                address_line="600 McCabe Road, La Porte, TX 77571"))
        db.commit()


    def test_postaddress(self):
        request_model = {
            "address_lines": "600 McCabe Road, La Porte, TX 77571",
            "name": "John Doe",
            "phone": "1234567890"
        }
        res=client.post("v1/address/add",json=request_model)
        self.assertEqual(res.status_code,200)

    def test_putaddress(self):
        request_model = {
            "name": "John Doe",
            "phone": "1234567890",
            "address_lines": "60 McCabe Road, La Porte, TX 77571"
        }
        res=client.put("v1/update/2",json=request_model)
        print(res.json())
        self.assertEqual(res.status_code,200)

    def test_deladdress(self):
        res=client.delete('/v1/delete/2')
        print(res.json())
        self.assertEqual(res.status_code,200)


