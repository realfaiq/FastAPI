from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool = False
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['htfc.com', 'icic.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode='before')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Age should be in between 0 and 100")


def insert_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Inserted into database")
    
    
patient_info = {'name': 'Faiq', 'email': 'abc@htfc.com', 'age': '24', 'weight': 75.2, 'allergies': ['dirrehea', 'Flu'], 'contact_details': {'email': 'abc@gmail.com', 'phone': '021-2215683'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)