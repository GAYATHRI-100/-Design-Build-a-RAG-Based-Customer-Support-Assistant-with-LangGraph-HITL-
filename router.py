import config

def calculate_confidence(docs):
    if not docs:
        return 0.0
    
    # Simple heuristic: more docs = higher confidence
    return min(len(docs) / config.TOP_K, 1.0)

def route_query(state):
    docs = state["docs"]
    confidence = calculate_confidence(docs)

    if confidence < config.CONFIDENCE_THRESHOLD:
        return "hitl"

    return "output"