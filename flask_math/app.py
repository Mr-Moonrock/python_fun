from flask import Flask, request

app = Flask(__name__)

def add(a,b):
    return int(a) + int(b)

def subtract(a,b):
    return int(a) - int(b)

def multiply(a,b):
    return int(a) * int(b)

def divide(a,b):
    return int(a) / int(b)

operations = {
    'add': add,
    'sub': subtract,
    'mult': multiply,
    'div': divide,
}

@app.route('/calculate')
def calculate():
    operation = request.args.get('op')
    a = request.args.get('a')
    b = request.args.get('b')

    if operation in operations:
        result = operations[operation](a,b)
        return f"<h1>{a} {operation} {b} = {result}</h1>"
    else: 
        return "<h1> Invalid operation</h1>"
    
if __name__ == '__main__':
    app.run()