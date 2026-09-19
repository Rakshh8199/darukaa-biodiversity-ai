from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.rag import search_knowledge

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Darukaa.Earth AI Biodiversity Chatbot is running!"
    }
from app.models import EnvironmentalInput, BiodiversityResponse
from app.reasoning import generate_recommendation
@app.post("/recommend", response_model=BiodiversityResponse)
def recommend(data: EnvironmentalInput):
    recommendation = generate_recommendation(data)

    return BiodiversityResponse(
        input_summary=data,
        recommendation=recommendation
    )

@app.get("/search")
def search(q: str):
    results = search_knowledge(q)

    return {
        "query": q,
        "results": results
    }