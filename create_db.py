import psycopg2, os

username = os.environ.get('USER')
password = input('Password: ')

def connect_db(dbname):
    db_params = {
        'dbname': dbname,
        'user': username,
        'password': password,
        'host': 'localhost',
        'port': '5432'
    }
    
    try:
        conn = psycopg2.connect(**db_params)
        conn.autocommit = True
        return conn
    
    except psycopg2.Error as e:
        print(f'Exception raised during database connection: {e}')
        return None

def create_db(dbname):
    conn = connect_db('postgres')
    if conn is None:
        return
    
    if not db_exists(conn, dbname):
        try:
            cursor = conn.cursor()
            cursor.execute(f'CREATE DATABASE {dbname}')
            
            print(f'[x] {dbname} created')
        
        except psycopg2.Error as e:
            print(f'Exception raised during database creation: {e}')
        
        finally:
            conn.close()

def db_exists(conn, dbname):
    cursor = conn.cursor()
    
    cursor.execute("SELECT datname FROM pg_database WHERE datname = %s;", (dbname,))
    result = cursor.fetchone()
    
    return result is not None

def create_table(conn, sql_file_path):
    try:
        with open(sql_file_path, 'r') as sql_file:
            sql = sql_file.read()
        
        with conn.cursor() as cur:
            cur.execute(sql)
            
        print('[x] Table created')
    
    except Exception as e:
        print(f'Exception raised during table creation: {e}')

if __name__ == '__main__':
    dbname = 'json2db'
    create_db(dbname)
    
    conn = connect_db(dbname)
    
    if conn is not None:
        create_table(conn, 'sql/create_table.sql')
        conn.close()
    
    print('All ran successfully')