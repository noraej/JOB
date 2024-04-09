# import os
# import json

# def find_files(directory):
#     for root, _, files in os.walk(directory):
#         for file in files:
#             if file.endswith(".json"):
#                 yield os.path.join(root, file)

# def check_stddev(file_path):
#     with open(file_path, 'r') as f:
#         data = json.load(f)
#         for result in data['results']:
#             if type(result['stddev']) is float: 
#                 if result['stddev'] > 1:
#                     return True
#     return False

# def main():
#     directory = 'test-results'  # Change this to your directory path
#     for file_path in find_files(directory):
#         if check_stddev(file_path):
#             print(file_path)

# if __name__ == "__main__":
#     main()
import os
import json

def find_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                yield os.path.join(root, file)

def calculate_mean(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        mean_values = [result['mean'] for result in data['results']]
        return sum(mean_values) / len(mean_values)

def main():
    directory = 'test-results'  # Change this to your directory path
    folder_mean = {}
    for file_path in find_files(directory):
        folder_name = os.path.dirname(file_path)
        if folder_name not in folder_mean:
            folder_mean[folder_name] = []
        folder_mean[folder_name].append(calculate_mean(file_path))

    for folder, mean_values in folder_mean.items():
        avg_mean = sum(mean_values) / len(mean_values)
        print(f"Folder: {folder}, Average Mean: {avg_mean}")

if __name__ == "__main__":
    main()