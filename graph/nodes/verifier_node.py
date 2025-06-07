# graph/nodes/verifier_node.py

def verifier_node(input_data: dict) -> dict:
    print("🧪 Verifier Agent checking code...")

    code = input_data["generated_code"]

    # List of potentially dangerous keywords
    unsafe_keywords = ["import os", "eval", "exec", "subprocess", "open", "socket", "__import__"]

    # Reject if any unsafe keywords are found
    if any(kw in code for kw in unsafe_keywords):
        return {
            **input_data,
            "verified": False,
            "verification_message": "❌ Code contains unsafe operations."
        }

    # Allow code that clearly uses SymPy
    uses_sympy = any(sym in code for sym in ["sympy", "symbols", "Eq", "solve"])

    # Allow simple math if it safely assigns to _result
    is_simple_math = "_result" in code and not any(bad in code for bad in unsafe_keywords)

    if uses_sympy or is_simple_math:
        return {
            **input_data,
            "verified": True,
            "verification_message": "✅ Code looks safe and valid."
        }

    # Default fallback: not verified
    return {
        **input_data,
        "verified": False,
        "verification_message": "❌ Code is neither SymPy-based nor basic arithmetic."
    }
