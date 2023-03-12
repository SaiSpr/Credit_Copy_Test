from fastapi import FastAPI, File, Query, UploadFile, HTTPException, Form
from fastapi.responses import FileResponse, PlainTextResponse
import uvicorn
import joblib
import numpy as np
from pydantic import BaseModel



app = FastAPI(
    title="Home Credit Loan Detection API",
    description="""An API that utilises a Machine Learning model that detects if a person is eligible for loan or not""",
    version="1.0.0", debug=True)


model = joblib.load('best_model_catboost.pkl')

@app.get("/", response_class=PlainTextResponse)
async def running():
  note = """
Home Credit Loan Detection API 🙌🏻

Note: add "/docs" to the URL to get the Swagger UI Docs or "/redoc"
  """
  return note

favicon_path = 'favicon.png'
@app.get('/favicon.png', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)
																	
# class fraudDetection(BaseModel):
#     step:int
#     types:int
#     amount:float	
#     oldbalanceorig:float	
#     newbalanceorig:float	
#     oldbalancedest:float	
#     newbalancedest:float	
#     isflaggedfraud:float

class fraudDetection(BaseModel):
    name_contract_type: int 
    children_count: int
    fam_members: int
    amt_credit_sum: float
    DAYS_INSTALMENT_delay: float
    amt_income_total: float
    credit_active: int
    bureau_year: int

# @app.post('/predict')
# def predict(data : fraudDetection):
                                                                                                                                                                                                                                
#     features = np.array([[data.step, data.types, data.amount, data.oldbalanceorig, data.newbalanceorig, data.oldbalancedest, data.newbalancedest, data.isflaggedfraud]])
#     model = joblib.load('credit_fraud.pkl')

#     predictions = model.predict(features)
#     if predictions == 1:
#         return {"fraudulent"}
#     elif predictions == 0:
#         return {"not fraudulent"}

@app.post('/predict')
def predict(data : fraudDetection):
                                                                                                                                                                                                                                
    features = np.array([[data.name_contract_type, data.children_count, data.fam_members, data.amt_credit_sum,
                          data.DAYS_INSTALMENT_delay, data.amt_income_total, data.credit_active, data.bureau_year]])
    

    predictions = model.predict(features)
    if predictions == 1:
        return {"The customer won't refund the loan"}
    elif predictions == 0:
        return {"The customer will refund his loan"}

cc.run_app(app=app)
