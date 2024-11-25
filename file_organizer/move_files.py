import os
import shutil

def move(folders, file_to_move):

    file_type = file_to_move["name"].split('.')[-1]

    parent_folder = os.path.basename(os.path.dirname(file_to_move["path"]))
    if parent_folder == file_type:
        return

    try:
        for item in folders:
            if (file_type == item["name"]):
                shutil.move(file_to_move["path"], item["path"])
                return
                

            # Create a folder if the needed folder doesn't exist already
        new_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Files", file_type)
        os.makedirs(new_folder_path, exist_ok=True)

        shutil.move(file_to_move["path"], new_folder_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_to_move['path']}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{file_to_move['path']}' or the destination folder.")
    except OSError as e:
        print(f"Unexpected error occurred: {e}")