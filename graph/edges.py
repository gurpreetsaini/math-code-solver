from langgraph.graph import StateGraph, END
from graph.nodes.input_node import input_node
from graph.nodes.explainer_node import explainer_node
from graph.nodes.verifier_node import verifier_node
from graph.nodes.executor_node import executor_node
from graph.nodes.output_node import output_node
from typing import TypedDict

# Define shared state for the graph
class GraphState(TypedDict):
    question: str
    reasoning: str
    generated_code: str
    verified: bool
    verification_message: str
    result: str
    final_output: str

# Initialize the LangGraph builder
builder = StateGraph(GraphState)

# Register all nodes
builder.add_node("input", input_node)
builder.add_node("explainer", explainer_node)
builder.add_node("verifier", verifier_node)
builder.add_node("executor", executor_node)
builder.add_node("output", output_node)

# Define the execution flow
builder.set_entry_point("input")
builder.add_edge("input", "explainer")
builder.add_edge("explainer", "verifier")
builder.add_edge("verifier", "executor")
builder.add_edge("executor", "output")
builder.add_edge("output", END)

# Compile the LangGraph
graph = builder.compile()

# Export the graph for Flask API use
app = graph
