import json
from pathlib import Path


# Location of our knowledge database
KNOWLEDGE_FILE = Path(__file__).parent.parent / "data" / "knowledge.json"


def load_knowledge():
    """Load environmental knowledge from knowledge.json."""
    with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def search_knowledge(query, number_of_results=3):
    """Find the most relevant knowledge for a user question."""

    knowledge = load_knowledge()

    query_words = set(query.lower().split())

    results = []

    for item in knowledge:

        searchable_text = (
            item["topic"]
            + " "
            + item["title"]
            + " "
            + item["content"]
            + " "
            + " ".join(item["metrics"])
        ).lower()

        score = 0

        for word in query_words:
            if word in searchable_text:
                score += 1

        if score > 0:
            results.append((score, item))

    # Highest matching score first
    results.sort(key=lambda x: x[0], reverse=True)

    return [item for score, item in results[:number_of_results]]