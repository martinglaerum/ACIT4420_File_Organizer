import move_files
import os
import re

def find_files(folder):
    files = []
    try:
        contents = os.listdir(folder)
    except FileNotFoundError:
        print(f"Error: The folder '{folder}' does not exist.")
        return files  # Return an empty list
    except PermissionError:
        print(f"Error: Permission denied when accessing the folder '{folder}'.")
        return files  # Return an empty list

    for file in contents:
        file_path = os.path.join(folder, file)
        file_info = {
            "name": file,
            "path": file_path,
        }
        files.append(file_info)
    return files

def main():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.join(BASE_DIR, "Files") 
    contents = os.listdir(base_path)

    try:
        contents = os.listdir(base_path)
    except FileNotFoundError:
        print(f'Error: The "Files" folder does not exist.')
        return []  # Return empty lists if the base directory is missing
    except PermissionError:
        print(f'Error: Permission denied when accessing the "Files" folder: {base_path}')
        return []  # Return empty lists if access is denied
    
    file_pattern = re.compile(r"^.+\.[a-zA-Z0-9]+$")
    files = []
    folders = []

    for item in contents:
        if file_pattern.match(item):  # Match the regex pattern
            file_path = os.path.join(base_path, item) 
            file_info = {
                "name": item,
                "path": file_path,
            }
            files.append(file_info)
        else:
            folder_path = os.path.join(base_path, item)
            folder_info = {
                "name": item,
                "path": folder_path,
            }
            folders.append(folder_info)
            files += find_files(folder_path)

    return (folders, files)