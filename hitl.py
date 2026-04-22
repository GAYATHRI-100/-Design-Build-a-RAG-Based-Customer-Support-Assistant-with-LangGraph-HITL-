def escalate_to_human(query):
    print("\n⚠️ Escalation Triggered (Low Confidence)")
    print(f"User Query: {query}")
    
    response = input("👨‍💻 Human Agent Response: ")
    return response