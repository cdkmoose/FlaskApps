import math
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

stack = []
func_map = {}

def argify(l):
    args = l.split(' ')
    for i in args:
        yield(i)

def add():
    stack.append(stack.pop() + stack.pop())
            
func_map['+'] = add

def subtract():
    x = stack.pop()
    stack.append( stack.pop() - x)
                            
func_map['-'] = subtract

def multiply():
    stack.append(stack.pop() * stack.pop())
                                       
func_map['*'] = multiply

def divide():
    x = stack.pop()
    stack.append(stack.pop() / x)
                                                        
func_map['/'] = divide

def root():
    stack.append(math.sqrt(stack.pop()))
                                                                    
func_map['v'] = root

def power():
    y = stack.pop()
    stack.append(pow(stack.pop(), y))

func_map['^'] = power


def process_op(op):
    func = func_map.get(op)
            
    if func is None:
        raise SyntaxError
    else:
        func()
                                                
def rpncalc(s):
    for arg in argify(s):
        if arg.isnumeric():
            stack.append(float(arg))
        else:
            if len(stack) < 1:
                raise ValueError
            else:
                process_op(arg)

    return stack.pop()

@app.route('/calc', methods=['GET'])
def calc():
    data = request.json
    expr = data['expr']

    return jsonify({'value': rpncalc(expr)})


@app.route('/')
def index():
        return 'Hello World!'


if __name__== '__main__':
    app.run(debug=True)
