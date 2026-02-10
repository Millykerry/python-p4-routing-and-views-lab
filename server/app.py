#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Route 1: Homepage
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Route 2: Print String
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print to console
    return parameter  # Show in browser

# Route 3: Count Numbers
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join([str(i) for i in range(parameter)])
    print(numbers)  # Print to console
    return numbers + '\n'  # Show in browser

# Route 4: Math Operations
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)