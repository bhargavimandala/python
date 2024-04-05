### List all the files in list of folders that user providers ###
### Read input from the user ###
### use for loop because user knows the particular executions ###
###  use module to perform this action ###


### to read input from the user we use command line, env variables and input ###
## input executes at the runtime

"""import os

folders = input("please provide list of folder names with spaces between:").split()
print(folders)
for folder in folders:
    # using OS module, it will talks to the operating system
    # in OS module, there is afunction called os.listdir to list of folders ###
    files = os.listdir(folder)
    print(files)


import os
folders = input("please provide folder names with space in between:").split()
#print(folders)
for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid foldername")   
        break
        print("=== list of files in folder -" +folder)
    ## to print all files in order ###
    for file in files:
        print(file)"""


####################

import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()               
    

