from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    html = """
    <html>
        <body>
            <h1>Hello, welcome to my page!</h1>
        </body>
    """
    return html

@app.route('/welcome')
def welcome():
    html = """
    <html>
        <body>
            <h1>Welcome!</h1>
        </body>
    """
    return html

@app.route('/welcome/home')
def welcome_home():
    html = """
    <html>
        <body>
            <h1>Welcome Home!</h1>
        </body>
    """
    return html

@app.route('/welcome/back')
def welcome_back():
    html = """
    <html>
        <body>
            <h1>Welcome Back!</h1>
        </body>
    """
    return html
