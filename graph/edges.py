# Define LangGraph edges connecting the nodes
from langgraph.graph import StateGraph, END
from graph.nodes.input_node import input_node
from graph.nodes.llm_node import llm_node
from graph.nodes.executor_node import executor_node
from graph.nodes.output_node import output_node
from typing import TypedDict

class GraphState(TypedDict):
    question: str
    explanation: str
    generated_code: str
    result: str

builder = StateGraph(GraphState)


builder.add_node("input", input_node)
builder.add_node("llm", llm_node)
builder.add_node("executor", executor_node)
builder.add_node("output", output_node)

# Define edges
builder.set_entry_point("input")
builder.add_edge("input", "llm")
builder.add_edge("llm", "executor")
builder.add_edge("executor", "output")
builder.add_edge("output", END)

# Build the graph
graph = builder.compile()
