from flask import Flask, jsonify

app = Flask(__name__)

# Dummy data for messages
messages = [
    {"id": 1, "sender": "Character A", "message": "Hello, how are you?", "timestamp": "10:00 AM"},
    {"id": 2, "sender": "Character B", "message": "I'm good, thank you! What about you?", "timestamp": "10:01 AM"},
    {"id": 3, "sender": "Character A", "message": "Doing great, excited to start this project.", "timestamp": "10:02 AM"}
]

@app.route('/api/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

if __name__ == '__main__':
    app.run(debug=True)
