from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from ml import ML

ml = None

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    global ml
    ml = ML()

'''
The class the post method accepts
'''
class Sequence(BaseModel):
    sequence: str

'''
A post method that takes in the sequence of the protein and sends it to the model before returning the prediction result
'''
@app.post("/sequence")
async def predict_sequence(sequence: Sequence):
    protein_sequence = sequence.sequence

    pred = ml.predict(protein_sequence)
    protein_structure = pred

    return {"structure": protein_structure}