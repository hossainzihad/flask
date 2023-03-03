from flask import Flask
import urllib.parse

app = Flask(__name__)

@app.route('/cal/<int:num1>/<string:op>/<int:num2>')
def calculator(num1, op, num2):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    elif op == '%':
        result = num1 % num2
    else:
        return "Invalid operator"

    # Decode URL-encoded operator
    op = urllib.parse.unquote(op)

    return f"{num1} {op} {num2} = {result}"

if __name__ == '__main__':
    app.run(debug=True)
