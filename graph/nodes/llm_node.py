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

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful Python tutor who ONLY returns raw Python code using SymPy. No explanations. No markdown. Just code."
            },
            {
                "role": "user",
                "content": f"Write Python code to solve this math problem using SymPy:\n{question}\n\nReturn ONLY the Python code. No markdown. No explanation."
            }
        ],
        stream=False
    )

    # Clean code: remove markdown fences if present
    generated_code = response.choices[0].message.content.strip()

    if generated_code.startswith("```"):
        lines = generated_code.splitlines()
        lines = [line for line in lines if not line.strip().startswith("```")]
        generated_code = "\n".join(lines).strip()

    print("📬 Cleaned code:\n", generated_code)

    return {
        "question": question,
        "generated_code": generated_code
    }
