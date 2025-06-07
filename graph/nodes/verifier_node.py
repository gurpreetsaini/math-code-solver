def verifier_node(input_data: dict) -> dict:
    print("🧪 Verifier Agent checking code...")

    code = input_data.get("generated_code", "")
    verified = True
    message = "✅ Code looks safe and valid."

    # Basic checks
    if "_result" not in code:
        verified = False
        message = "❌ Code does not assign _result."

    if "import os" in code or "import sys" in code or "open(" in code:
        verified = False
        message = "❌ Code contains unsafe operations."

    if not code.strip().startswith("from sympy") and "symbols(" not in code:
        verified = False
        message = "❌ Code doesn't appear to use SymPy properly."

    return {
        **input_data,
        "verified": verified,
        "verification_message": message
    }
