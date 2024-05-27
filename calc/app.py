# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_nums():
    '''
    Add the a and b parameters together
    '''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a,b)
    
    return str(result)
    
@app.route('/sub')
def sub_nums():
    '''
    Subtract the a and b parameters
    '''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a,b)
    
    return str(result)
    
@app.route('/mult')
def mult_nums():
    '''
    Multiply the a and b parameters togther
    '''    
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))    
    result = mult(a,b)
    
    return str(result)
    
@app.route('/div')
def div_nums():
    '''
    Divide the a and b parameters
    '''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a,b)
    
    return str(result)