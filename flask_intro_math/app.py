from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Hello, World!'

@app.route('/add')
def addition():
    """Add a and b"""
    a = request.args.get('a')
    b = request.args.get('b')
    result = int(a) + int(b)
    return f"<h1>{a} + {b} = {result} </h1>"

@app.route('/sub')
def subtraction():
    """Subtract b from a"""
    a = request.args.get('a')
    b = request.args.get('b')
    result = int(a) - int(b)
    return f"<h1>{a} - {b} = {result} </h1>"

@app.route('/mult')
def multiplication():
    """Multiply a and b"""
    a = request.args.get('a')
    b = request.args.get('b')
    result = int(a) * int(b)
    return f"<h1>{a} * {b} = {result} </h1>"

@app.route('/div')
def division():
    """Divide a and b"""
    a = request.args.get('a')
    b = request.args.get('b')
    result = int(a) / int(b)
    return f"<h1>{a} / {b} = {result} </h1>"

if __name__ == '__main__':
    app.run()