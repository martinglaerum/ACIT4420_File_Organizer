import sys
import os

        # Ensure the parent directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import find_files_and_folder
import move_files

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
            # Finds all files and folders and their path
        folders, files = find_files_and_folder.main()
            # Moves all the files
        for item in files:
            move_files.move(folders, item)

if __name__ == '__main__':
    main()
