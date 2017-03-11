from flask import Flask
app = Flask(__name__)

@app.route('/')
def create_mock():
    return 'Hello, World! This is the first run of webmock'
