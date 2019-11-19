from datetime import datetime
import time
from flask import Flask, request

app = Flask(__name__)
messages = [
        {'username': 'John', 'time': time.time(), 'text': 'Hello!'},
        {'username': 'Mary', 'time': time.time(), 'text': 'Hi!'},
]
password_storage = {
    'John': '12345',
    'Mary': '54321'
}

@app.route('/')
def start():
    return 'fok u'

@app.route('/time')
def time_now():
    return datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    # return "lol"

@app.route('/send', methods=['POST'])
def sending():
    '''
    JSON{"username": str, "password": str, "text": str}
    username, text - непустые строки
    :return: {'ok': bool}
    '''

    username = request.json['username']
    password = request.json['password']
    text = request.json['text']

    if username not in password_storage:
        password_storage[username] = password

    if not isinstance(username,str) or len(username) == 0:
        return {'ok': False}
    if not isinstance(text, str) or len(text) == 0:
        return {'ok': False}
    if password_storage[username] != password:
        return {'ok': False}

    messages.append({'username': username,
                     'time': time.time(),
                     'text': text})
    return {'ok': True}

@app.route('/messages')
def msgs():
    after = float(request.args['after'])
    filtered_msg = [message for message in messages if message['time'] > after]
    return {'messages': filtered_msg}

app.run()