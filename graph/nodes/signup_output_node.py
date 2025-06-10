def signup_output_node(input_data: dict) -> dict:
    parent_name = input_data.get("parent_name", "")
    questionnaire = input_data.get("questionnaire", "")
    final_output = f"Hello {parent_name}, please answer the following questions:\n{questionnaire}"
    input_data["final_output"] = final_output
    return input_data
