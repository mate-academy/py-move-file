import os


def move_file(command) -> None:
    
    parts = command.split(" ")
    if len(parts) != 3  or parts[0] != "mv":
        raise ValueError("Invalid command")
    
    sourse_file = parts[1]
    destination = ' '.join(parts[2:])

    if not os.path.exists(sourse_file):
        raise FileNotFoundError("Error")
    
    destination_dir = os.path.dirname(destination)
    if not os.path.exists(destination):
        os.makedirs(destination_dir)
    
    if os.path.isdir(destination):
        dest_file = os.path.join(destination, os.path.basename(sourse_file))
    else:
        dest_file = destination

    os.rename(sourse_file, dest_file)
    os.remove(sourse_file)

    print(f"File moved successfully from {sourse_file} to {dest_file}")
