import os
import shutil

# Define file type categories and their extensions
FILE_TYPES = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    "Documents": ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    "Audio": ['.mp3', '.wav', '.aac', '.flac'],
    "Videos": ['.mp4', '.mov', '.avi', '.mkv'],
    "Archives": ['.zip', '.rar', '.tar', '.gz', '.7z'],
    "Scripts": ['.py', '.js', '.html', '.css', '.sh', '.bat'],
    # Add more categories and extensions as needed
}

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension in lowercase
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # Find the category for this extension
        moved = False
        for category, extensions in FILE_TYPES.items():
            if ext in extensions:
                dest_dir = os.path.join(folder_path, category)
                os.makedirs(dest_dir, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_dir, filename))
                print(f"Moved '{filename}' to '{category}/'")
                moved = True
                break

        # If extension not found in categories, move to 'Others'
        if not moved:
            dest_dir = os.path.join(folder_path, "Others")
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_dir, filename))
            print(f"Moved '{filename}' to 'Others/'")

def main():
    folder = input("Enter the path of the folder to organize: ").strip()
    organize_files(folder)
    print("Organization complete.")

if __name__ == "__main__":
    main()


