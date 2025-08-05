from pydantic import BaseModel, EmailStr, AnyUrl, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool = False
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = self.weight / (self.height ** 2)
        return bmi
    

def insert_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print('BMI' ,patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Inserted into database")
    
    
patient_info = {'name': 'Faiq', 'email': 'abc@htfc.com', 'age': '65', 'weight': 75.2, 'height': 12, 'allergies': ['dirrehea', 'Flu'], 'contact_details': {'email': 'abc@gmail.com', 'emergency': '021-2215683'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)