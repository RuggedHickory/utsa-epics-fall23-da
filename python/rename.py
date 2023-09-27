import os

def rename_images(folder_path):
    image_formats = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']  # Add more formats if needed
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and os.path.splitext(f)[1].lower() in image_formats]
    
    if not image_files:
        print("No image files found in the folder.")
        return
    
    image_files.sort()  # Sort the files to ensure sequential renaming
    
    for index, old_name in enumerate(image_files, start=1):
        extension = os.path.splitext(old_name)[1]
        new_name = f"Daniel_{index:03d}{extension}"
        os.rename(os.path.join(folder_path, old_name), os.path.join(folder_path, new_name))
        print(f"Renamed {old_name} to {new_name}")

if __name__ == "__main__":
    folder_path = "C:\\Users\\dagui\\OneDrive\\python"  
    rename_images(folder_path)
