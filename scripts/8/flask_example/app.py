from flask import Flask, make_response, render_template, request, redirect
from hashlib import sha256
import random

SALT = "h1kcoqjf019v0fk"
def hash(plain_text):
    plain_text = SALT + plain_text
    return sha256(plain_text.encode()).hexdigest()


# print(hash("1234"))
# print(hash('admin'))
# print(hash('pass123'))

app = Flask(__name__)


db = {
    'majed': '8aa03f14ec1b6f21dc3a1742ca7d1538c91fc3b293b5b4d7ce621ad076c3eb02',
    'ahmad': '468e5f8cd95ddd5f97de6c6b180d3cc58feff98aa0b626f7b21d1a404b514d92',
    'omar': 'e04dd94abe581bb4640769d67d6553aa391fedb51639604c30eaea770aea8a71'
}

tokens_db = {}
"""

{
    "random_token": "username"
}

"""


posts_db = []


def get_user() -> str:
    """
        Return an empty string if the user is not logged in
        Return username if the user is logged in
    """
    cookie = request.headers['Cookie']
    if "; token" not in cookie:
        return ''
    token = cookie.split('; token=')[1]
    if token in tokens_db:
        return tokens_db[token]
    return ''
    # request.headers



def add_post(text: str) -> None:
    posts_db.append(text)

def create_token(username: str) -> str:
    new_token = [random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(20)]
    new_token = "".join(new_token)
    tokens_db[new_token] = username
    return new_token
    

def check_credentials(username: str, password: str) -> bool:
    if username in db and db[username] == hash(password):
        return True
    return False


@app.route('/')
def home():
    if get_user():
        return redirect('/posts')
    return redirect('/login')

@app.route('/posts')
def posts():
    username = get_user()
    print("Username >>>>>>>>>>>>>>>>", username)
    return render_template('posts.html', posts=posts_db, username=username)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    """
        request.args is used for get parameters only however we know that POST request is the recommended method to use logging in.
        for post data use request.form when using HTML or request.json for REST APIs more on that later.

    """
    username = request.form['username']
    password = request.form['password']

    if check_credentials(username, password):
        resp = make_response(redirect('/posts'))
        resp.set_cookie('token', create_token(username))
        return resp
    
    else:
        return render_template('login.html', error='Wrong username/password')



@app.route('/create-post', methods=['POST'])
def create_post():
    post_text = request.form['text']
    add_post(post_text)

    return render_template('posts.html', message = 'Created successfully', posts=posts_db)

app.run(debug=True)

