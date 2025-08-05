from pydantic import BaseModel

class address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str = 'Male'
    age: int
    address: address
    

address_dict = {'city': 'peshawar', 'state': 'KP', 'pin': '25000'}
address1 = address(**address_dict)

patient_dict = {'name': 'Faiq', 'age': 24, 'address': address1}

patient1 = Patient(**patient_dict)

# temp = patient1.model_dump()
# temp = patient1.model_dump_json()
# temp = patient1.model_dump(include=['name', 'gender'])
# temp = patient1.model_dump(exclude={'address': ['state']})
temp = patient1.model_dump(exclude_unset=True)

print(temp)
print(type(temp))