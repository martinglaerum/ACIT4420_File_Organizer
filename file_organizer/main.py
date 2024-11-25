import sys
import os

        # Ensure the parent directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import find_files_and_folder
import move_files
import file_structure

def main():

        # Introduction to the program
    print("This module includes some folders and some diffrent file types.")
    print("These files are positioned in completely random folders, and one of the file types don't have a folde to move to")
    print(f'To sort these files into their appropiate folders, enter "sort"')
    print(f'To exit the program, enter "exit".\n')
    while True:
        choice = input("Enter your choice:  ")
        if choice in ["sort", "exit"]:
            break
        choice = input("Invalid choice, try again:  ")

        # Sorts all the files in to the correct folders
    if(choice == "sort"):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        base_path = os.path.join(BASE_DIR, "Files") 
        print("---- File structure before sorting ----")
        print("files/")
        file_structure.print_directory_structure(base_path, indent="│   ")
            # Finds all files and folders and their path
        folders, files = find_files_and_folder.main()
            # Moves all the files
        for item in files:
            move_files.move(folders, item)
        print("\n\n---- File structure after sorting ----")
        print("files/")
        file_structure.print_directory_structure(base_path, indent="│   ")

if __name__ == '__main__':
    main()
