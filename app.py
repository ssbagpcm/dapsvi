from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

client = Groq(api_key="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")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "user",
                "content": message
            }
        ],
        temperature=0.1,
        max_tokens=5000,
        top_p=1,
        stream=True,
        stop=None,
    )

    response = ""
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""

    return jsonify({'response': response}), 200, {'ContentType': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True)
