def output_node(input_data: dict) -> dict:
    print("📤 Output node finalizing response...")

    # Extract data from previous nodes
    question = input_data.get("question", "")
    reasoning = input_data.get("reasoning", "")
    code = input_data.get("generated_code", "")
    result = input_data.get("result", "")
    verified = input_data.get("verified", False)
    verification_message = input_data.get("verification_message", "")

    # Build the final output string
    if not verified:
        final_output = f"""❌ Code verification failed:
{verification_message}
"""
    else:
        final_output = f"""✅ Question: {question}

🧠 Reasoning:
{reasoning}

📜 Code:
{code}

🧪 Verification:
{verification_message}

✅ Final Result:
{result}
"""

    # Add final_output to the state for frontend use
    input_data["final_output"] = final_output
    return input_data
