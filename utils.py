def execute_script_file(filepath, conn):
    with open(filepath, 'r') as file:
        script = file.read()
        file.close()
        conn.executescript(script)
        conn.commit()

def insert(url, conn):
    script = f"INSERT INTO news(news_url) VALUES('{url}');"
    conn.executescript(script)
    conn.commit()

def update(id, conn):
    script = f"UPDATE news set processed=1 where id={id};"
    conn.executescript(script)
    conn.commit()

def get_single(id, conn):
    script = f"SELECT * FROM news WHERE id={id};"
    cursor = conn.cursor()
    cursor.execute(script)
    r = cursor.fetchall()[0]
    cursor.close()
    return r

def get_unprocessed(conn):
    script = "SELECT * FROM news WHERE processed=0;"
    cursor = conn.cursor()
    cursor.execute(script)
    r = cursor.fetchall()
    cursor.close()
    return r
