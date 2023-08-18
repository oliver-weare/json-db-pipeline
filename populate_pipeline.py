import json, os, glob, psycopg2

username = os.environ.get('USER')
password = input('Password: ')

print('Trying connection')

try:
    conn = psycopg2.connect(
        host='localhost',
        database='json2db',
        user=username,
        password=password
    )
    
    print('Connection succeeded')
    
except psycopg2.Error as e:
    print(f'Exception raised: {e}')

files_dir = 'json'
sql = "INSERT INTO json_data (data) VALUES (%s)"

print('Trying glob and populate')

try:
    files_paths = glob.glob(os.path.join(files_dir, '*.json'))
    
    with conn.cursor() as cur:
        for path in files_paths:
            with open(path, "r") as json_file:
                data = json.load(json_file)
                cur.execute(sql, (json.dumps(data),))
        conn.commit()
    
    conn.close()
    
    print('Extracted and loaded successfully')
    
except Exception as e:
    print(f'Exception raised: {e}')

