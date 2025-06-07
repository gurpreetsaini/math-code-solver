def verifier_node(input_data: dict) -> dict:
    print("🧪 Verifier Agent checking code...")

    code = input_data["generated_code"]

    # Lowercase and split into lines for stricter line-by-line validation
    code_lines = code.strip().lower().splitlines()

    # Critical unsafe patterns (cleaned of whitespace for detection)
    unsafe_keywords = [
        "importos", "__import__('os')", "__import__(\"os\")",
        "eval", "exec", "subprocess", "open", "socket"
    ]

    # Check each line individually
    for line in code_lines:
        cleaned_line = line.replace(" ", "")
        if any(bad in cleaned_line for bad in unsafe_keywords):
            return {
                **input_data,
                "verified": False,
                "verification_message": "❌ Code contains unsafe operations."
            }

    # Allow if clearly using SymPy
    uses_sympy = any(sym in code for sym in ["sympy", "symbols", "Eq", "solve"])

    # Allow safe simple math fallback
    is_simple_math = "_result" in code and not any(
        bad in code.replace(" ", "").lower() for bad in unsafe_keywords
    )

    if uses_sympy or is_simple_math:
        return {
            **input_data,
            "verified": True,
            "verification_message": "✅ Code looks safe and valid."
        }

    # Default fallback: reject unclear or suspicious code
    return {
        **input_data,
        "verified": False,
        "verification_message": "❌ Code is neither SymPy-based nor basic arithmetic."
    }
