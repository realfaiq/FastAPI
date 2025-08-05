from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Name of the patient", description="Give the name of the patient in less than 50 characters", examples=["Faiq", "Ahmad"])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: bool = Annotated[bool, Field(default=None, description="Is the patient married or not.")]
    allergies: Annotated[Optional[List[str]], Field(default = None, max_length=5)]
    contact_details: Dict[str, str]


def insert_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Inserted into database")
    

def update_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print("Updated")
    
# patient_info = {'name': 'Faiq', 'age': '24', 'weight': 75.2, 'married': True, 'allergies': ['Pollen', 'Dust'], 'contact_details': {'email': 'abc@gmail.com', 'phone': '021-2215683'}}
patient_info = {'name': 'Faiq', 'email': 'abc@gmail.com', 'linkedin_url': 'https://linkedin.com', 'age': '24', 'weight': 75.2, 'contact_details': {'email': 'abc@gmail.com', 'phone': '021-2215683'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)