from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route('/temps')

def hello_world():
    return 'Hello world'