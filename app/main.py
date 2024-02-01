import os


def move_file(command) -> None:
    
    parts = command.split(" ")
    if len(parts) != 3  or parts[0] != "mv":
        raise ValueError("Invalid command")
    
    source_file = parts[1]
    destination = ' '.join(parts[2:])

    if destination.endswith("/"):
        if not os.path.exists(destination):
            os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source_file))
    else:
        if not os.path.exists(os.path.dirname(destination)):
            os.makedirs(os.path.dirname(destination), exist_ok=True)

    try:
        with open(source_file, "rb") as src_file:
            content = src_file.read()
        with open(destination, "wb") as dst_file:
            dst_file.write(content)
    
        os.remove(source_file)
        print(f"Moved {source_file} to {destination}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"What the ...error")
