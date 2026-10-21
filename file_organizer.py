# Import the os module to handle file paths, directories, and listing files
import os
# Import the shutil module to handle moving files from one location to another
import shutil

# Define the function that scans and organizes files within a target directory
def organize_folder(target_dir):
    # Check if the path provided by the user actually exists on the computer
    if not os.path.exists(target_dir):
        # Print an error message if the folder path is wrong or missing
        print("The specified directory does not exist.")
        # Stop running the function immediately
        return

    # Create a mapping plan that defines which file extensions go into which folders
    # Form requirement highlights explicit separation for Images, PDFs, Videos, and Documents
    EXTENSION_MAP = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'PDFs': ['.pdf'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.flv'],
        'Documents': ['.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Audio': ['.mp3', '.wav', '.aac'],
        'Archives': ['.zip', '.rar', '.7z']
    }

    # Initialize an empty dictionary to keep track of how many files we move into each folder
    summary = {}
    
    # Loop through every file and folder name inside the target directory
    for item in os.listdir(target_dir):
        # Build the full absolute path for the current item
        item_path = os.path.join(target_dir, item)
        
        # Make sure the current item is a file (we don't want to move folders inside folders)
        if os.path.isfile(item_path):
            # Split the filename to extract its file extension (e.g., '.png') and convert to lowercase
            _, file_ext = os.path.splitext(item)
            file_ext = file_ext.lower()
            
            # Set a default fallback folder category if the file type doesn't match our map
            destination_folder = 'Others'
            
            # Loop through our rules to find a folder matching this file's extension
            for category, extensions in EXTENSION_MAP.items():
                # Check if the current file extension is in the category's list
                if file_ext in extensions:
                    # Assign the correct category folder name
                    destination_folder = category
                    # Break out of the inner loop early since we found a match
                    break
            
            # Build the full absolute path for where the new organized category folder should be
            dest_dir_path = os.path.join(target_dir, destination_folder)
            
            # Check if that category folder does not exist yet
            if not os.path.exists(dest_dir_path):
                # Create the new folder dynamically
                os.makedirs(dest_dir_path)
            
            # Try to safely move the file into its new folder
            try:
                # Perform the move operation from the old path to the new folder path
                shutil.move(item_path, os.path.join(dest_dir_path, item))
                # Add 1 to the counter for this specific folder category in our summary
                summary[destination_folder] = summary.get(destination_folder, 0) + 1
            # Catch any unexpected file errors (like files locked by another program)
            except Exception as e:
                # Print a warning notice showing which file failed to move
                print(f"Could not move {item}: {e}")

    # Print a clean, formatted text header for the final tracking summary
    print("\n=== FILE ORGANIZATION SUMMARY ===")
    # Check if no files were found or moved during the scan
    if not summary:
        # Inform the user that the folder was already empty or organized
        print("No files were moved.")
    # If files were successfully sorted
    else:
        # Loop through each category and its total count in the summary dictionary
        for folder, count in summary.items():
            # Print a neat summary bullet showing the work done
            print(f" Organized {count} file(s) into the '{folder}' folder.")
    # Print a closing visual divider bar
    print("=================================")

# Check if this script is being run directly by Python rather than being imported elsewhere
if __name__ == '__main__':
    # Prompt the user to type or paste the exact path of the messy folder they want organized
    folder_to_clean = input("Enter the absolute path of the folder to organize: ").strip()
    # Call the organization function using the provided path
    organize_folder(folder_to_clean)
