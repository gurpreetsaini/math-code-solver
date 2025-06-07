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

    # Initialize
    explanation = ""
    generated_code = ""

    # Try Markdown-based format first
    if "```python" in full_output:
        try:
            parts = full_output.split("```python")
            explanation = parts[0].strip()
            code_block = parts[1].split("```")[0]
            generated_code = code_block.strip()
        except Exception as e:
            print("⚠️ Markdown parsing failed, trying fallback...")
    else:
        # Fallback 1: Look for Reasoning: and Code:
        if "Reasoning:" in full_output and "Code:" in full_output:
            try:
                reason_part = full_output.split("Reasoning:")[1]
                if "Code:" in reason_part:
                    explanation, raw_code = reason_part.split("Code:")
                    explanation = explanation.strip()
                    generated_code = raw_code.strip()
                else:
                    explanation = reason_part.strip()
            except Exception as e:
                print("⚠️ Fallback split by Reasoning/Code failed")
                explanation = ""
                generated_code = full_output.strip()
        else:
            # Fallback 2: Treat whole output as code
            generated_code = full_output.strip()
            explanation = "(No explanation provided)"

    print("📖 Explanation:\n", explanation)
    print("📬 Generated code:\n", generated_code)

    return {
        "question": question,
        "explanation": explanation,
        "generated_code": generated_code
    }
