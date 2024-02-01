import os


def move_file(command) -> None:
    
    parts = command.split(" ")
    if len(parts) != 3  or parts[0] != "mv":
        raise ValueError("Invalid command")
    
    sourse_file = parts[1]
    destination = ' '.join(parts[2:])

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(sourse_file))
    else:
        if os.path.dirname(destination):
            os.makedirs(os.path.dirname(destination), exist_ok=True)
    
    try:
        with open(sourse_file, "rb") as src_file:
            content = src_file.read()
        with open(destination, "wb") as dst_file:
            dst_file.write(content)
    
        os.remove(sourse_file)
        print(f"Moved {sourse_file} to {destination}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"What the ...error")
