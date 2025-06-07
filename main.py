from graph.edges import graph

if __name__ == "__main__":
    input_data = {"question": "Integrate sin(x) * cos(x)"}
    
    print("🚀 Starting LangGraph math code solver...")
    result = graph.invoke(input_data)
    
    print("✅ Final Output:")
    print(result)
