import sys
import traceback

def executor_node(input_data: dict) -> dict:
    """
    Safely execute the generated Python code and return the result,
    including the explanation.
    """
    generated_code = input_data["generated_code"]
    local_vars = {}

    try:
        print("🧪 Executing generated code...")

        # Append _result = ... if not explicitly defined
        if "_result" not in generated_code:
            last_line = generated_code.strip().splitlines()[-1]
            generated_code += f"\n_result = {last_line}"

        exec(generated_code, {}, local_vars)
        result = local_vars.get("_result", None)

        print("✅ Execution result:", result)

        return {
            "question": input_data.get("question"),
            "explanation": input_data.get("explanation", ""),
            "generated_code": generated_code,
            "result": str(result)
        }

    except Exception as e:
        print("❌ Error during code execution:")
        traceback.print_exc()
        return {
            "question": input_data.get("question"),
            "explanation": input_data.get("explanation", ""),
            "generated_code": generated_code,
            "result": None,
            "error": str(e)
        }
