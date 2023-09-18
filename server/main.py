import json
from flask import Flask, jsonify, request
import openai
import os
from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'creds.json'

app = Flask(__name__)

# Initialize the OpenAI API with your key.
with open(file_location, "r") as file:
    credentials = json.load(file)


openai.api_key = credentials["OPENAI_API_KEY"]

@app.route('/generate_question', methods=['POST'])
def generate_question():
    # Get the prompt from the client.
    data = request.json
    prompt = data.get('prompt', '')

    # Check if prompt is provided.
    if not prompt:
        return jsonify({"error": "Please provide a prompt."}), 400

    # Generate a question using OpenAI API.
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "assistant", "content": f"Here is 10 educational question about: {prompt} in JSON form [{{q: question, a: answer}}]. The questions are factual, contextual and specific."}
            ],
            temperature = 0.5
        )
        question = response.choices[0].message.content.strip()
        return jsonify({"question": question, "debug": response})
    except Exception as e:
        return jsonify({"error": "Internal error. %s" % e}), 500



if __name__ == '__main__':
    app.run(debug=True)
