import psycopg2, os

from create_db import connect_db

def display_rows(conn, table):
    try:
        with conn.cursor() as cur:
            cur.execute(f'SELECT * FROM {table}')
            rows = cur.fetchall()
            
            if rows:
                for row in rows:
                    print(row)
            
            else:
                print('No rows in table')
    
    except psycopg2.Error as e:
        print(f'Exception raised during row collection: {e}')

if __name__ == '__main__':
    dbname = 'json2db'
    conn = connect_db(dbname)
    
    if conn is not None:
        display_rows(conn, 'json_data')
        conn.close()