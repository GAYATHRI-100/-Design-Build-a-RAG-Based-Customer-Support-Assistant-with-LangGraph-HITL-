from langgraph.graph import StateGraph
from modules.llm import generate_answer
from modules.hitl import escalate_to_human
from modules.router import route_query

# ---------------- PROCESS NODE ----------------
def process_node(state):
    query = state["query"]
    retriever = state["retriever"]

    docs = retriever.invoke(query)

    return {
        "query": query,
        "docs": docs,
        "retriever": retriever
    }

# ---------------- OUTPUT NODE ----------------
def output_node(state):
    answer = generate_answer(state["query"], state["docs"])
    return {"answer": answer}

# ---------------- HITL NODE ----------------
def hitl_node(state):
    answer = escalate_to_human(state["query"])
    return {"answer": answer}

# ---------------- BUILD GRAPH ----------------
def build_graph():
    workflow = StateGraph(dict)

    workflow.add_node("process", process_node)
    workflow.add_node("output", output_node)
    workflow.add_node("hitl", hitl_node)

    workflow.set_entry_point("process")

    workflow.add_conditional_edges(
        "process",
        route_query,
        {
            "output": "output",
            "hitl": "hitl"
        }
    )

    return workflow.compile()