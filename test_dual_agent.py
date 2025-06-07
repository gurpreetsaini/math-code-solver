from graph.nodes.input_node import input_node
from graph.nodes.explainer_node import explainer_node
from graph.nodes.verifier_node import verifier_node

def test_pipeline(question):
    print("\n🧠 INPUT:", question)

    # Step 1: input node
    input_data = input_node({"question": question})

    # Step 2: explainer node
    explainer_data = explainer_node(input_data)
    print("\n📜 EXPLAINER OUTPUT:")
    print("Reasoning:\n", explainer_data["reasoning"])
    print("Generated Code:\n", explainer_data["generated_code"])

    # Step 3: verifier node
    verified_data = verifier_node(explainer_data)
    print("\n🧪 VERIFIER OUTPUT:")
    print("Verified:", verified_data["verified"])
    print("Message:", verified_data["verification_message"])

# Example usage
if __name__ == "__main__":
    test_pipeline("Solve 2x squared minus 8 equals 0")
