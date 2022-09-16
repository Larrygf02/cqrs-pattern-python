import psycopg2

def insert_db(payload):
    conn = get_connection()
    cursor = conn.cursor()
    payload['precio'] = float(payload['precio'])
    print(list(payload.values()))
    cursor.execute("INSERT INTO products (name, cantidad, precio) values(%s, %s, %s) returning id;", list(payload.values()))
    result = cursor.fetchone()
    conn.commit()
    conn.close()
    return result

def get_connection():
    conn = psycopg2.connect("dbname=sync-demo user=postgres password=admin")
    return conn
    