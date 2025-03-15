import os

# Get the current working directory
directory = os.getcwd()

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a Python file and contains spaces
    if filename.endswith(".py") and " " in filename:
        # Construct new filename by replacing spaces with underscores
        new_filename = filename.replace(" ", "_")
        
        # Construct full file paths
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        
        # Rename the file
        try:
            os.rename(old_path, new_path)
            print(f'Renamed: "{filename}" -> "{new_filename}"')
        except Exception as e:
            print(f"Error renaming {filename}: {e}")

print("Renaming complete.")
