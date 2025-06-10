from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from graph.edges import app as langgraph_app
from graph.signup_edges import signup_app

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
    "reasoning": result.get("reasoning", ""),
    "generated_code": result.get("generated_code", ""),
    "verification_message": result.get("verification_message", ""),
    "verified": result.get("verified", False),
    "result": result.get("result", ""),
    "final_output": result.get("final_output", "")  # ✅ THIS LINE IS CRUCIAL
})

@app.route("/stream_explainer", methods=["POST"])
def stream_explainer():
    data = request.get_json()
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "No question provided"}), 400

    from graph.nodes.explainer_node import explainer_node_stream
    def generate():
        for chunk in explainer_node_stream({"question": question}):
            yield chunk
    return Response(generate(), mimetype="text/plain")

@app.route("/signup_questionnaire", methods=["POST"])
def signup_questionnaire():
    data = request.get_json()
    parent_name = data.get("parent_name", "")
    if not parent_name:
        return jsonify({"error": "No parent name provided"}), 400
    result = signup_app.invoke({"parent_name": parent_name})
    return jsonify({
        "parent_name": parent_name,
        "questionnaire": result.get("questionnaire", ""),
        "final_output": result.get("final_output", "")
    })


if __name__ == "__main__":
    app.run(debug=True)
