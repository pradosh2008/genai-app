from flask import Flask, request, jsonify
from config import load_config
from openai import OpenAI

basic_chatbot_app = Flask(__name__)


config = load_config()

openai_client = OpenAI(
    api_key=config['openai']['api_key'],
    organization ='org-zy91VcIKogamLudMARObBJbb'
)

@basic_chatbot_app.route('/', methods=['GET'])
def index():
    return "Welcome to the Chatbot API!"

@basic_chatbot_app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['prompt']
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.9,
    )
    return jsonify({"response": response.choices[0].message.content.strip()})

if __name__ == '__main__':
    basic_chatbot_app.run(debug=True)



