from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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

    #TODO Use model and get predicted structure

    protein_structure = "TODO: Predicted secondary structure from model"

    return {"structure": protein_structure}