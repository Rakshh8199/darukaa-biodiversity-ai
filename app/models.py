from pydantic import BaseModel
from typing import Optional


class EnvironmentalInput(BaseModel):
    soil_organic_carbon: float
    rainfall: str
    crop: str
    region: str
    temperature: Optional[float] = None
    soil_moisture: Optional[float] = None


class Recommendation(BaseModel):
    recommendation: str
    why_it_works: str
    impacted_metrics: list[str]
    time_horizon: str
    evidence: list[str]


class BiodiversityResponse(BaseModel):
    input_summary: EnvironmentalInput
    recommendation: Recommendation