import os
import json

def find_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                yield os.path.join(root, file)

def check_stddev(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        for result in data['results']:
            if type(result['stddev']) is float: 
                if result['stddev'] > 1:
                    return True
    return False

def main():
    directory = 'test-results'  # Change this to your directory path
    for file_path in find_files(directory):
        if check_stddev(file_path):
            print(file_path)

if __name__ == "__main__":
    main()