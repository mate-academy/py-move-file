import os
import shutil

def move_file(command) -> None:
    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command")
    
    source_file = parts[1]
    destination = ' '.join(parts[2:])

    # Check if the destination directory is 'dir' and if it exists, remove it
    if destination.startswith('dir') and os.path.exists('dir'):
        shutil.rmtree('dir')
    
    # Check if the destination ends with a slash or is an existing directory
    if destination.endswith("/") or (os.path.isdir(destination) and not os.path.isfile(destination)):
        os.makedirs(destination, exist_ok=True)
        destination_file = os.path.join(destination, os.path.basename(source_file))
    else:
        # Ensure the destination's parent directory exists
        parent_dir = os.path.dirname(destination)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir, exist_ok=True)
        destination_file = destination
    
    # Move the file by copying and then deleting
    if os.path.abspath(source_file) != os.path.abspath(destination_file):
        try:
            # Copy the file
            with open(source_file, 'rb') as src, open(destination_file, 'wb') as dst:
                dst.write(src.read())
            
            # Delete the source file
            os.remove(source_file)
            print(f"Moved '{source_file}' to '{destination_file}'")
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
    else:
        print("Source and destination are the same. No action taken.")
