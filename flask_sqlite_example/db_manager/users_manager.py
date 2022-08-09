import sqlite3
import hashlib

SALT = 'ajkfFjk17fAO1#'
def hash(plain_text: str) -> str:
    return hashlib.sha256((SALT+plain_text).encode()).hexdigest()


def create_user(username: str, password: str, fname: str, lname: str) -> None:
    conn = sqlite3.connect('notes.db')
    cur = conn.cursor()
    cur.execute(f'''INSERT INTO User VALUES('{username}', '{hash(password)}', '{fname}', '{lname}');
                ''')
    # insert into user values('majedlutfi96', '1234', 'majed','lutfi');
    conn.commit() # used for write operations only
    conn.close()
    
def validate_credentials(username: str, password: str) -> bool:
    conn = sqlite3.connect('notes.db')
    cur = conn.cursor()
    cur.execute(f'''SELECT * FROM User where username = '{username}' and password='{hash(password)}';
                ''')
    users = cur.fetchall()
    conn.close()
    return len(users) > 0
    # if len(users) > 0:
    #     return True
    # else:
    #     return False
    

def user_exists(username: str) -> bool:
    conn = sqlite3.connect('notes.db')
    cur = conn.cursor()
    cur.execute(f'''SELECT * FROM User where username = '{username}';
                ''')
    users = cur.fetchall()
    conn.close()
    return len(users) > 0

def delete_user(username: str) -> None:
    conn = sqlite3.connect('notes.db')
    cur = conn.cursor()   
    cur.execute(f'''DELETE FROM User where username = '{username}';
                ''')
    conn.commit()
    conn.close()