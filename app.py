from flask import Flask, request, jsonify,render_template
from basic_chatbot.chatbot import get_response
from basic_chatbot.config import load_config
from openai import OpenAI

app = Flask(__name__)

config = load_config()

openai_client = OpenAI(
    api_key=config['openai']['api_key']
)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['prompt']
    response = get_response(openai_client , user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)

