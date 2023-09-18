import json

def parse_response_json(response) -> dict:
    """Parse the response from the OpenAI API and return the question."""
    question = json.loads(response.choices[0].message.content.strip())
    return question