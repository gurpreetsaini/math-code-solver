from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

def questionnaire_node(input_data: dict) -> dict:
    """Generate a questionnaire for the parent."""
    parent_name = input_data["parent_name"]
    with open("prompts/parent_questionnaire_prompt.txt", "r", encoding="utf-8") as f:
        prompt_template = f.read()
    prompt = prompt_template.replace("{parent_name}", parent_name)
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a friendly assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    questionnaire = response.choices[0].message.content.strip()
    return {
        "parent_name": parent_name,
        "questionnaire": questionnaire
    }
