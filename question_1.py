#question 1 task 1 

import os 

def directory_list(path):
    try:
        if os.path.isdir(path):
            print(f"Contents of the directory '{path}:")
            for item in os.listdir(path):
                print(item)
        else:
            print(f"The path '{path}' is not a valid directory.")
    except PermissionError:
        print(f"Permission denied, Cannot access '{path}'.")
    except FileNotFoundError:
        print(f"Could not find '{path}'.")
    except Exception as e:
        print(f"An error occured: {e}")

if __name__=="__main__":
    user = input("Please enter a path: ")
    directory_list(user)