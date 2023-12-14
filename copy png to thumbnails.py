import os
import shutil

source_dir = r"C:\Users\Xieon\Desktop\repositories\new private\test\master_pkmnpic\Pokedex"
destination_dir = r"C:\Users\Xieon\Desktop\repositories\new private\test\master_pkmnpic\Xieon's Gaming Corner Specific\Thumbnails"

for folder_name in os.listdir(source_dir):
    folder_path = os.path.join(source_dir, folder_name)

    if os.path.isdir(folder_path):
        _, pokemon_name = folder_name.split(" ", 1)
        dest_folder_path = os.path.join(destination_dir, pokemon_name)
        os.makedirs(dest_folder_path, exist_ok=True)

        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            if os.path.isfile(file_path) and file_name.lower().endswith('.png'):
                dest_file_path = os.path.join(dest_folder_path, file_name)

                # Check if the file already exists in the destination folder
                if os.path.exists(dest_file_path):
                    base, extension = os.path.splitext(file_name)
                    counter = 1

                    # Add a suffix to the file name until a unique name is found
                    while os.path.exists(os.path.join(dest_folder_path, f"{base}_{counter}{extension}")):
                        counter += 1

                    # Append the counter to the file name
                    base = f"{base}_{counter}"

                    # Construct the new file name
                    new_file_name = f"{base}{extension}"
                    dest_file_path = os.path.join(dest_folder_path, new_file_name)

                # Copy the file to the destination folder
                shutil.copy(file_path, dest_file_path)
