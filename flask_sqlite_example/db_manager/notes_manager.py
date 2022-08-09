import sqlite3

def add_note(username: str, title: str, content: str) -> None:
    conn = sqlite3.connect('notes.db')
    cur = conn.cursor()
    cur.execute(f'''INSERT INTO Post VALUES('{username}', '{title}', '{content}')
                ;''')
    conn.commit()
    conn.close()
    
def delete_note(username: str, title: str) -> None:
    conn = sqlite3.connect('notes.db')
    cur = conn.cursor()
    cur.execute(f'''DELETE FROM Post where username='{username}' and title = '{title}';
                ''')
    conn.commit()
    conn.close()
    
    
def validate_title(username: str, title: str) -> bool:
    conn = sqlite3.connect('notes.db')
    cur = conn.cursor()
    cur.execute(f'''SELECT * FROM Post where username='{username}' and title = '{title}';
                ''')
    posts = cur.fetchall()
    conn.close()
    return len(posts) == 0
    # if len(posts) == 0:
    #     return True
    # else:
    #     return False