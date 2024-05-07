import sqlite3

def execute_script_file(filepath, conn):
    with open(filepath, 'r') as file:
        script = file.read()
        file.close()
        conn.executescript(script)
        conn.commit()

def insert(url, source, title, published,  conn:sqlite3.Connection):
    #script = f"INSERT INTO news(news_url, source, title, published_date) VALUES('{url}', '{source}', '{title}', '{published}');"
    script = f"INSERT INTO news(news_url, source, title, published_date) VALUES(?, ?, ?, ?);"
    t = (url, source, title, published)
    try:
        conn.execute(script, t)
        conn.commit()
    except sqlite3.OperationalError:
        print(script)
        raise sqlite3.OperationalError

def update(id, summary, conn):
    script = f'UPDATE news set processed=1, summary="{summary}" where id={id};'
    conn.executescript(script)
    conn.commit()

def get_single(id, conn):
    script = f"SELECT * FROM news WHERE id={id};"
    cursor = conn.cursor()
    cursor.execute(script)
    r = cursor.fetchall()[0]
    cursor.close()
    return r

def get_unprocessed(conn, single=False):
    script = "SELECT * FROM news WHERE processed=0;"
    if single:
        script = "SELECT * FROM news WHERE processed=0 ORDER BY id DESC LIMIT 1"
    cursor = conn.cursor()
    cursor.execute(script)
    r = cursor.fetchall()
    cursor.close()
    return r

def get_processed(conn, amount, page):
    script = f"SELECT * FROM news WHERE processed=1 LIMIT {page*amount}, {amount};"
    cursor = conn.cursor()
    cursor.execute(script)
    r = cursor.fetchall()
    cursor.close()
    return r
