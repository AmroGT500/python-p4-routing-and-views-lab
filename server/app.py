from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_text(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count_range(parameter):
    count = '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n' 
    return count

@app.route('/math/<int:num1>/<op>/<int:num2>')
def do_math(num1, op, num2):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == 'div':
        result = num1 / num2
    elif op == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
