import os
import re

def find_files(folder):
    files = []

        # List all files in the subdirectory of "Files"
    try:
        contents = os.listdir(folder)
    except FileNotFoundError:   # Subdirectory doesn't exist 
        print(f"Error: The folder '{folder}' does not exist.")
        return files
    except PermissionError: # Can't acces the subdirectory
        print(f"Error: Permission denied when accessing the folder '{folder}'.")
        return files

        # Store all files in the subdirectory
    for file in contents:
        file_path = os.path.join(folder, file) # Path to the file
        file_info = {
            "name": file,
            "path": file_path,
        }
        files.append(file_info)
    return files

def main():
        # Find path of "Files"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.join(current_dir, "Files") 

    try:
            # List the content of "Files"
        contents = os.listdir(base_path)
    except FileNotFoundError: # "Files" folder doesn't exist
        print(f'Error: The "Files" folder does not exist.')
        return [] 
    except PermissionError: # Can't access the "Files" folder
        print(f'Error: Permission denied when accessing the "Files" folder: {base_path}')
        return [] 

        # Regex pattern to seperate folders from files
    pattern = re.compile(r"^.+\.[a-zA-Z0-9]+$")

    files = []
    folders = []

        # Store all files and folders
    for item in contents:
        if pattern.match(item):  # Match the regex pattern
            file_path = os.path.join(base_path, item) # Path to the file
            file_info = {
                "name": item,
                "path": file_path,
            }
            files.append(file_info)
        else:
            folder_path = os.path.join(base_path, item) # Path to the folder
            folder_info = {
                "name": item,
                "path": folder_path,
            }
            folders.append(folder_info) 
            files += find_files(folder_path)    # Store all files stored inside the folder

    return (folders, files)
