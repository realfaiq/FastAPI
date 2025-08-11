from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Literal, Annotated
import pickle
import pandas as pd

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
    

app = FastAPI()

class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the user")]
    income: Annotated[int, Field(..., gt=0, description="Income of the user")]
    loan_amount: Annotated[int, Field(..., gt=0, description="Loan Amount Requested")]
    credit_score: Annotated[int, Field(..., gt=0, description="Credit Score of the user")]
    years_employed: Annotated[int, Field(..., gt=0, description="How many years the users has been employed")]
    has_defaulted_before: Annotated[Literal[0, 1], Field(..., description="Has the user ever defaulted 0 if not and 1 if Yes")]
    

@app.post('/predict')
def predict_eligiblity(data: UserInput):
    input_df = pd.DataFrame([{
        'age': data.age,
        'income': data.income,
        'loan_amount': data.loan_amount,
        'credit_score': data.credit_score,
        'years_employed': data.years_employed,
        'has_defaulted_before': data.has_defaulted_before
    }])
    prediction = int(model.predict(input_df)[0])
    predict = "Not-Eligible"
    if prediction == 1:
        predict = "Eligible"
    return JSONResponse(status_code=200, content={'predicted_category': predict})