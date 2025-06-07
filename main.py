from graph.nodes.input_node import input_node
from graph.nodes.llm_node import llm_node
from graph.nodes.executor_node import executor_node

if __name__ == "__main__":
    input_data = {"question": "Write Python code to differentiate sin(x)"}

    step1 = input_node(input_data)
    print("✅ input_node output:", step1)

    print("⏳ Sending to DeepSeek...")
    step2 = llm_node(step1)
    print("✅ DeepSeek response:", step2)

    print("🧪 Running code...")
    step3 = executor_node(step2)
    print("✅ Final result:", step3)
