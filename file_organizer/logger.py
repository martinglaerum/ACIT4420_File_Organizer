import os
import datetime

    # Finds the absolute path to the current file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def log_info(file, folder):
    file_path = os.path.join(BASE_DIR, "log.txt") # Specifies the path to the log file
    print(file, folder, file_path)
        # Opens the log file and stores info about each file that was moved
    with open(file_path, "at") as f:
        f.write(f"Time: {datetime.datetime.now().replace(microsecond=0)}, The file {file} was moved to the folder {folder}\n")