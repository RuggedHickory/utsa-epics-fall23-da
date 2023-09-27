import os
import shutil

def organize_images(source_folder, destination_root_folder, num_folders):
    image_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
    image_files.sort()
    
    if not image_files:
        print("No image files found in the folder.")
        return
    
    images_per_folder = len(image_files) // num_folders
    
    for folder_index in range(num_folders):
        folder_name = f"folder_{folder_index + 1}"
        folder_path = os.path.join(destination_root_folder, folder_name)
        
        os.makedirs(folder_path, exist_ok=True)
        
        start_index = folder_index * images_per_folder
        end_index = start_index + images_per_folder
        
        if folder_index == num_folders - 1:
            end_index = len(image_files)
        
        for index in range(start_index, end_index):
            source_file = os.path.join(source_folder, image_files[index])
            destination_file = os.path.join(folder_path, image_files[index])
            
            shutil.move(source_file, destination_file)
            print(f"Moved {image_files[index]} to {folder_path}")

if __name__ == "__main__":
    source_folder = "C:\\Users\\dagui\\OneDrive\\python"  # Replace with source folder path
    destination_root_folder = "C:\\Users\\dagui\\OneDrive\\1-50"  # Replace with destination root folder path
    num_folders = 5  # Number of folders
    
    organize_images(source_folder, destination_root_folder, num_folders)
