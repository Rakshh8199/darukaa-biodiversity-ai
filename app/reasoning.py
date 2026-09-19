from app.models import EnvironmentalInput, Recommendation


def generate_recommendation(data: EnvironmentalInput) -> Recommendation:

    impacted_metrics = [
        "soil organic carbon",
        "biodiversity",
        "habitat diversity",
        "water availability"
    ]

    if data.soil_organic_carbon < 0.5 and data.rainfall.lower() == "low":
        recommendation = (
            "Introduce agroforestry and intercropping instead of relying "
            "on a single crop."
        )

        why = (
            "Low soil organic carbon indicates poor soil condition, while "
            "low rainfall increases water stress. Adding trees and multiple "
            "crop species can improve soil organic matter, provide habitat, "
            "reduce erosion, and improve resilience to water stress."
        )

        horizon = "2-5 years"

    else:
        recommendation = (
            "Increase crop and habitat diversity using intercropping, "
            "native vegetation, and soil-conservation practices."
        )

        why = (
            "Increasing vegetation diversity can support more organisms "
            "while improving soil and water-related ecosystem functions."
        )

        horizon = "1-5 years"

    evidence = [
        "FAO — Agroecology and biodiversity resources",
        "IPCC — Climate Change and Land",
        "FAO — Soil organic carbon and soil health resources"
    ]

    return Recommendation(
        recommendation=recommendation,
        why_it_works=why,
        impacted_metrics=impacted_metrics,
        time_horizon=horizon,
        evidence=evidence
    )