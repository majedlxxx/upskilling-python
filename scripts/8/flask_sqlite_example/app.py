from crypt import methods
from flask import Flask, render_template, request, redirect, make_response
import db_manager


db_manager.build_db()
app = Flask(__name__)


def get_user() -> str:
    """
        This function returns username if the user is logged in, or empty string if the user is not logged in
    """
    if 'token' not in request.cookies:
        return ""
    token = request.cookies['token']
    return db_manager.get_user_from_token(token)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    
    if db_manager.validate_credentials(username, password):
        resp = make_response(redirect('/notes'))
        resp.set_cookie('token', db_manager.create_token(username))
        return resp
    else: 
        return render_template('login.html', error="Wrong username/password"), 401
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    username = request.form['username']
    fname = request.form['fname']
    lname = request.form['lname']
    password = request.form['password']
    password2 = request.form['password2']
    
    if db_manager.user_exists(username):
        return render_template('signup.html', error="User already exists"), 409

    if password != password2:
        return render_template('signup.html', error="Passwords don't match"), 400
    
    db_manager.create_user(username, password, fname, lname)
    return redirect('/login')

@app.route('/notes', methods=["GET", "POST"])
def notes():
    if get_user():
        return render_template('notes.html')
    else:
        return redirect('/login')

app.run(debug=True)