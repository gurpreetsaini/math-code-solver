def signup_input_node(input_data: dict) -> dict:
    """First node for parent sign up. Validates parent name."""
    parent_name = input_data.get("parent_name", "").strip()
    if not parent_name:
        raise ValueError("No parent name provided.")
    print(f"[Signup Input Node] Received parent name: {parent_name}")
    return {"parent_name": parent_name}
