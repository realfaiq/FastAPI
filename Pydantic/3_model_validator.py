from pydantic import BaseModel, EmailStr, AnyUrl, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool = False
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Patients older than 60 must have an emergency contact")
    

def insert_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Inserted into database")
    
    
patient_info = {'name': 'Faiq', 'email': 'abc@htfc.com', 'age': '65', 'weight': 75.2, 'allergies': ['dirrehea', 'Flu'], 'contact_details': {'email': 'abc@gmail.com', 'emergency': '021-2215683'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)