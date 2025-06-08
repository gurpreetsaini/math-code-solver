from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

def explainer_node(input_data: dict) -> dict:
    print("🧠 Explainer Agent called...")

    question = input_data["question"]

    with open("prompts/code_generation_prompt.txt", "r", encoding="utf-8") as f:
        prompt_template = f.read()

    prompt = prompt_template.replace("{question}", question)

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful math explainer who teaches children step by step."},
            {"role": "user", "content": prompt}
        ],
        stream=True
    )

    # Stream and accumulate the output
    full_output = ""
    for chunk in response:
        if hasattr(chunk, 'choices') and chunk.choices and hasattr(chunk.choices[0], 'delta'):
            delta = chunk.choices[0].delta
            if hasattr(delta, 'content') and delta.content:
                full_output += delta.content

    # Separate reasoning and code
    reasoning = ""
    code = ""

    if "```python" in full_output:
        parts = full_output.split("```python")
        reasoning = parts[0].strip()
        code = parts[1].split("```")[0].strip()
    else:
        reasoning = full_output
        code = "# No code block found"

    return {
        "question": question,
        "reasoning": reasoning,
        "generated_code": code
    }

def explainer_node_stream(input_data: dict):
    question = input_data["question"]
    with open("prompts/code_generation_prompt.txt", "r", encoding="utf-8") as f:
        prompt_template = f.read()
    prompt = prompt_template.replace("{question}", question)
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful math explainer who teaches children step by step."},
            {"role": "user", "content": prompt}
        ],
        stream=True
    )
    for chunk in response:
        if hasattr(chunk, 'choices') and chunk.choices and hasattr(chunk.choices[0], 'delta'):
            delta = chunk.choices[0].delta
            if hasattr(delta, 'content') and delta.content:
                yield delta.content
