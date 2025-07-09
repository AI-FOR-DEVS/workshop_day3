from flask import Flask, request, jsonify, render_template
from app import chat

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def query():
    data = request.json
    query = data.get('query')

    response = chat(query)
    return jsonify({'response': response})

if __name__ == '__main__':  
    app.run(debug=True, port=8080)