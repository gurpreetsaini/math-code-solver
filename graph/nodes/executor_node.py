import sys
import traceback

def executor_node(input_data: dict) -> dict:
    """
    Safely execute the generated Python code and return the result.
    """
    generated_code = input_data["generated_code"]
    local_vars = {}

    try:
        print("🧪 Executing generated code...")

        # Append _result = ... to capture final expression
        if not generated_code.strip().endswith("_result"):
            generated_code += "\n_result = " + generated_code.strip().splitlines()[-1]

        exec(generated_code, {}, local_vars)

        result = local_vars.get("_result", None)

        print("✅ Execution result:", result)

        return {
            "question": input_data["question"],
            "generated_code": generated_code,
            "result": str(result)
        }

    except Exception as e:
        print("❌ Error during code execution:")
        traceback.print_exc()
        return {
            "question": input_data["question"],
            "generated_code": generated_code,
            "result": None,
            "error": str(e)
        }
