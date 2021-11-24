from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to Web Application !!</h1><br><h2> Have a Nice Day !</h2>'

app.run(host='0.0.0.0', port=7077)
