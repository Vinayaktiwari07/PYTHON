import os

def print_directory_contents(directory):
    try:
        # Get the list of all files and directories in the specified directory
        contents = os.listdir(directory)
        
        print(f"Contents of the directory '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{directory}'.")

if __name__ == "__main__":
    # Specify the directory you want to list
    directory_path = input("Enter the directory path: ")
    print_directory_contents(directory_path)
