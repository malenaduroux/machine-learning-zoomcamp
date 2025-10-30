import pickle

from fastapi import FastAPI
import uvicorn

from typing import Dict, Any

client = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}


with open('wk05-homework/pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

code = FastAPI(title="lead-scoring-prediction")

def predict_single(client):
    result = pipeline.predict_proba(client)[0, 1]
    return float(result)

@code.post("/predict")
def predict(client: Dict[str, Any]):
    prob = predict_single(client)

    return {
        "Conversion Probability": prob,
        "Converted?": bool(prob >= 0.5)
    }

if __name__ == "__main__":
    uvicorn.run(code, host="0.0.0.0", port=9696)