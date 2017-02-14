from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/hello')
def hello():
    return 'Hello!'

@app.route('/user/<username>')
def show_user(username):
    return 'User {}'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

@app.route('/login', method=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        return request.form['username']
    else:
        return 'Invalid user'
