from .notes_manager import *
from .tokens_manager import *
from .users_manager import *

def build_db() -> None:
    """
        Create all tables.
    """
    conn = sqlite3.connect('notes.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS User(
        username VARCHAR(200),
        password CHAR(64),
        fname VARCHAR(256),
        lname VARCHAR(256)
    );''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS Token(
        username VARCHAR(200),
        token CHAR(20)
    );''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS Post(
        username VARCHAR(200),
        title VARCHAR(256),
        content VARCHAR(10000)
    );''')
    conn.commit()
    conn.close()
    
