def input_node(input_data: dict) -> dict:
    """
    First node: receives user math question.
    """
    question = input_data.get("question", "").strip()

    if not question:
        raise ValueError("No question provided.")

    print(f"[Input Node] Received question: {question}")
    return {
        "question": question
    }
