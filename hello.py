from flask import Flask
from flask import url_for
from flask import request 
from flask import render_template

from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_word():
    return "Hello, World!"

@app.route('/hello/')
@app.route('/hello/<name>/')
def magic(name=None):
    return render_template("magic.html", name=name)

@app.route('/magictoo/<name>')
def magictoo():
    naam = "Dion Dresschers"
    return render_template("magic.html", naam=naam)    

@app.route('/user/<username>')
def show_user(username):
    return "Hello %s" % escape(username)

@app.route('/help/')
def help():
    return "help"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "dit is een POST, doe de login"
    else:
        return "Dit is een GET, dus laat het login formulier zien"
#with app.test_request_context():
#    print(url_for('help'))
#    #print(url_for('show_user', username='peter'))

@app.route('/request_test/')
def request_test():
    test = request
    render_template('request_test.html', test=test)
