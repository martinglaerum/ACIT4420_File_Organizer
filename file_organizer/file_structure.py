import os

    # Prints the directory structure of "Files"
def print_structure(path, indent=""):
    items = os.listdir(path)
    items.sort()

    for index, item in enumerate(items):
        item_path = os.path.join(path, item)
        is_last = index == len(items) - 1

            # Use '└──' for the last item, '├──' for others
        prefix = "└── " if is_last else "├── "

        if os.path.isdir(item_path):
            print(f"{indent}{prefix}{item}/")
                # Recursively print subdirectories
            new_indent = indent + ("    " if is_last else "│   ")
            print_structure(item_path, new_indent)
        else:
            print(f"{indent}{prefix}{item}") # Print the file name