import os
import shutil
import logger

def move(folders, file_to_move):
        # Finds the file type
    file_type = file_to_move["name"].split('.')[-1]

        # Checks if the file is alredy in the correct folder
    parent_folder = os.path.basename(os.path.dirname(file_to_move["path"]))
    if parent_folder == file_type:
        return

        # Tries to move the file
    try:
            # Finds the correct folder and moves the file
        for item in folders:
            if (file_type == item["name"]):
                shutil.move(file_to_move["path"], item["path"])
                logger.log_info(file_to_move["name"], item["name"]) # Log the moved file
                return
                
            # Create a folder if the needed folder doesn't exist already
        new_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Files", file_type)
        os.makedirs(new_folder_path, exist_ok=True)
        shutil.move(file_to_move["path"], new_folder_path)  # Move the file to the new folder
        logger.log_info(file_to_move["name"], file_type) # Log the moved file
    except FileNotFoundError: # File to move doesn't exist
        print(f"Error: The file '{file_to_move['path']}' does not exist.")
    except PermissionError: # Can't move the file
        print(f"Error: Permission denied when accessing '{file_to_move['path']}' or the destination folder.")
    except OSError as e:    # Unexpected error
        print(f"Unexpected error occurred: {e}")
