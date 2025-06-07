from flask import Flask, request, jsonify
from flask_cors import CORS
from graph.edges import app as langgraph_app

app = Flask(__name__)
CORS(app)  # ✅ Allow frontend HTML to call this API

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    question = data.get("question", "")

    if not question:
        return jsonify({"error": "No question provided"}), 400

    result = langgraph_app.invoke({"question": question})

    return jsonify({
        "question": question,
        "reasoning": result.get("llm_output", ""),
        "generated_code": result.get("generated_code", "")
    })

if __name__ == "__main__":
    app.run(debug=True)
