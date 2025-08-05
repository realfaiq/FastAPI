from pydantic import BaseModel

class address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: address
    

address_dict = {'city': 'peshawar', 'state': 'KP', 'pin': '25000'}
address1 = address(**address_dict)

patient_dict = {'name': 'Faiq', 'gender': 'male', 'age': 24, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1.name)
print(patient1.gender)
print(patient1.age)
print(patient1.address.city)