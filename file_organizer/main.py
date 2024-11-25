import find_files_and_folder
import move_files

def main():

    print("This module includes 4 diffrent folder representing 5 different file types.")
    print("There are 15 different files, three of each file type. This includes a file type which does not have a folder.")
    print("Currently these files are all positioned in completely random folders")
    print("This is the current file structure:")
    print(f'To sort these files into their appropiate folders, enter "sort"')
    print(f'To un-sort these files into random folders, enter "randomize"')
    print(f'To exit the program, enter "exit".\n')
    while True:
        choice = "sort" #input("Enter your choice:  ")
        if choice in ["sort", "randomize", "exit"]:
            break
        choice = input("Invalid choice, try again:  ")


    if(choice == "sort"):
        folders, files = find_files_and_folder.main()
        for item in files:
            move_files.move(folders, item)
    elif(choice == "randomize"):
        a = 1
    else:
        a = 2 

if __name__ == '__main__':
    main()
