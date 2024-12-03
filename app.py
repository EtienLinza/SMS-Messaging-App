from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import sqlite3
import uuid

# Initialize Flask and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Database setup
def init_db():
    conn = sqlite3.connect('sms.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_number TEXT,
            to_number TEXT,
            message TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_sms():
    data = request.json
    from_number = data['from_number']
    to_number = data['to_number']
    message = data['message']

    # Save to database
    conn = sqlite3.connect('sms.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO messages (from_number, to_number, message) 
        VALUES (?, ?, ?)
    ''', (from_number, to_number, message))
    conn.commit()
    conn.close()

    # Emit message to all clients
    socketio.emit('new_message', {
        'from_number': from_number,
        'to_number': to_number,
        'message': message
    })

    return jsonify({"status": "Message sent"}), 200

@app.route('/inbox/<number>')
def inbox(number):
    conn = sqlite3.connect('sms.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM messages WHERE to_number = ?', (number,))
    messages = cursor.fetchall()
    conn.close()
    return jsonify(messages)

# Initialize database
init_db()

# Run server
if __name__ == '__main__':
    socketio.run(app, debug=True)