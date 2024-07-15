#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<parameter>')
def count(parameter):
    num = int(parameter)
    html = ""
    for n in range(num):
       p = f"{n}\n"
       html += p

    return html

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if operation == "+":
        return str(int(num1) + int(num2))
    elif operation == "-":
        return str(int(num1) - int(num2))
    elif operation == "*":
        return str(int(num1) * int(num2))
    elif operation == "div":
        return str(int(num1) / int(num2))
    elif operation == "%":
        return str(int(num1) % int(num2))

if __name__ == '__main__':
    app.run(port=5555, debug=True)
