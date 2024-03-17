import os
import shutil

def move_file(command):
    # Split the command into parts
    parts = command.split()

    # Check if the command has at least two arguments
    if len(parts) < 3:
        print("Invalid command. Please provide source and destination paths.")
        return

    # Extract source and destination paths
    source_path = parts[1]
    dest_path = parts[2]

    # Check if the source file exists
    if not os.path.exists(source_path):
        print(f"Error: {source_path} does not exist.")
        return

    # Check if the destination directory exists
    if dest_path.endswith('/'):
        dest_dir = dest_path
    else:
        dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Move the file
    shutil.move(source_path, dest_path)

# Test the function
move_file("mv file.txt first_dir/second_dir/third_dir/file2.txt")
print(open("first_dir/second_dir/third_dir/file2.txt").read())

# Clean up: Remove the source file
try:
    os.remove("file.txt")
except FileNotFoundError:
    pass
