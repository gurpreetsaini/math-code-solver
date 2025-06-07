

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

def llm_node(input_data: dict) -> dict:
    print("🚀 LLM node was called")

    question = input_data["question"]

    # Load chain-of-thought prompt template
    with open("prompts/code_generation_prompt.txt", "r", encoding="utf-8") as f:
        prompt_template = f.read()

    prompt = prompt_template.replace("{question}", question)

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful math tutor."},
            {"role": "user", "content": prompt}
        ],
        stream=False
    )

    full_output = response.choices[0].message.content.strip()

    # Parse response: separate explanation and code
    explanation = ""
    generated_code = ""

    if "```python" in full_output:
        parts = full_output.split("```python")
        explanation = parts[0].strip()
        code_block = parts[1].split("```")[0]
        generated_code = code_block.strip()
    else:
        # fallback if no markdown formatting
        generated_code = full_output.strip()

    print("📖 Explanation:\n", explanation)
    print("📬 Generated code:\n", generated_code)

    return {
        "question": question,
        "explanation": explanation,
        "generated_code": generated_code
    }
