from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! This is Mashood Khan speaking" 
