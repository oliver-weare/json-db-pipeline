import json, os, random

for i in range(1, 1001):
    try:
        file_path = f'json/{i}.json'
        
        if os.path.exists(file_path):
            print(f'File {i}.json deleted')
            os.remove(file_path)
        
        data = {
            "random_number": random.randint(1, 10000000000000)
        }
        
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file)
        
        print(f'File {i}.json created')
    
    except Exception as e:
        print(f'Problem with iteration {i}: {e}')
