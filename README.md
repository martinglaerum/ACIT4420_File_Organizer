# ACIT4420_File_Organizer

This project is part of an assignement in the course ACIT4420. **ACIT4420_File_Organizer** is a tool that will automatically sort all files in a specified directory based on their file extension. To use the program simply move around the files in the "Files" directory. The files can be in any of the subdirectories or in the **Files** directory. It's also possible to delete some of the subdirectories, or create new file types.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)
## Features
- Sorts existing files into corresponding folders
- Creates new folders if needed
- Prints the file structure before and after it has sorted the files
## Installation
To get started, follow these steps:
1. **Clone the Repository** (or download the package):
   ```bash
   git clone https://github.com/martinglaerum/ACIT4420_File_Organizer.git
   cd ACIT4420_File_Organizer
   ```
2. **Create a Virtual Environment** (recommended):
   ```bash
   python3 -m venv gameenv
   source gameenv/bin/activate  # On Windows, use `gameenv\Scripts\activate`
   ```
3. **Install the Package**:
   ```bash
   pip install -e .
   ```
## Usage
Once installed, you can use the tool by running the following command in your terminal:
```bash
file_organizer
```
This will launch a menu where you can choose one of the following
1. **Sort Files**
2. **Exit**
Choosing **Sort Files** will automatically sort the files in the **Files** folder. Choosing **Exit** stops the program.
## Project Structure
Here is a brief overview of the project's structure:
```
ACIT4420_File_Organizer/
│
├── file_organizer/
│   ├── __init__.py
│   ├── main.py                # Entry point for the program
│   ├── find_files_and_folder.py
│   ├── move_files.py
│   ├── file_structure.py
│   ├── Files
│
├── setup.py                   # Installation script
└── README.md                  # Project documentation (this file)
```
### Key Files:
- **`main.py`**: Contains the main function that launches the program.
- **`setup.py`**: Script for installing the package.
- **`find_files_and_folder.py`**: Finds all files and folders
- **`move_files.py`**: Moves all files to the correct folder
- **`file_structure.py`**: Prints the filestructure in the **Files** folder
- **`Files`**: Folder containing alle the unsorted files and folders
