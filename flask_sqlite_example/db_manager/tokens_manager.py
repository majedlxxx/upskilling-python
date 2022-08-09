from pydoc import importfile
import sqlite3
import random

def create_token(username: str) -> str:
    token = [random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(20)]
    token = "".join(token)
    conn = sqlite3.connect('notes.db')
    cur = conn.cursor()   
    cur.execute(f'''INSERT INTO Token VALUES('{username}', '{token}');
                ''')
    conn.commit()
    conn.close()
    return token
    
def delete_token(username: str) -> None:
    conn = sqlite3.connect('notes.db')
    cur = conn.cursor()   
    cur.execute(f'''DELETE FROM Token where username = '{username}';
                ''')
    conn.commit()
    conn.close()
    
def get_user_from_token(token: str) -> str:
    conn = sqlite3.connect('notes.db')
    cur = conn.cursor()   
    cur.execute(f'''SELECT username, token FROM Token where token='{token}';
                ''')
    username = cur.fetchone()
    conn.close()
    if not username: #username == None
        return ""
    return username[0]
    
