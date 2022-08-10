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
    # request.headers['cookies']
    return db_manager.get_user_from_token(token)
    
    
@app.route('/', methods=["GET"])
def home():
    if get_user():
        return redirect('/notes')
    return redirect('/login')

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
    username = get_user()
    if not username:
        return redirect('/login')
    
    if request.method == "GET":
        return render_template('notes.html', notes=db_manager.get_notes(username), username=username)
    
    title = request.form['title']
    content = request.form['content']
    
    if not db_manager.validate_title(username, title):
        return render_template('notes.html', error="You have used this title before", notes=db_manager.get_notes(username), username=username)
    db_manager.add_note(username, title, content)
    
    return render_template('notes.html', message="Created successfully", notes=db_manager.get_notes(username), username=username)
    

@app.route('/logout', methods=['GET'])
def logout():
    resp = make_response(redirect('/login'))
    # resp.set_cookie('token'. '')
    resp.delete_cookie('token')
    return resp
app.run(debug=True)