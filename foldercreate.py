import os

def create_folders_from_file(file_path, directory_path):
    with open(file_path, 'r') as file:
        name_list = [line.strip() for line in file]

    for name in name_list:
        folder_path = os.path.join(directory_path, name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
        else:
            print(f"Folder already exists: {folder_path}")

if __name__ == "__main__":
    # Input path to the text file containing names
    file_path = r"H:\Xieons Gaming Corner Full Ecosystem\Created Graphics\New\names.txt"

    # Input directory path
    directory_path = input("Enter the directory path: ")

    # Call the function to create folders
    create_folders_from_file(file_path, directory_path)
