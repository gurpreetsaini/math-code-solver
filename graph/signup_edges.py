from langgraph.graph import StateGraph, END
from typing import TypedDict

from graph.nodes.signup_input_node import signup_input_node
from graph.nodes.questionnaire_node import questionnaire_node
from graph.nodes.signup_output_node import signup_output_node

class SignupState(TypedDict):
    parent_name: str
    questionnaire: str
    final_output: str

builder = StateGraph(SignupState)

builder.add_node("signup_input", signup_input_node)
builder.add_node("questionnaire", questionnaire_node)
builder.add_node("signup_output", signup_output_node)

builder.set_entry_point("signup_input")
builder.add_edge("signup_input", "questionnaire")
builder.add_edge("questionnaire", "signup_output")
builder.add_edge("signup_output", END)

signup_graph = builder.compile()

signup_app = signup_graph
