import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        operation, source_file, destination_path = command.split()
        if operation == "mv":
            if "/" not in destination_path:
                destination_file = destination_path
            elif destination_path.endswith("/"):
                os.makedirs(destination_path, exist_ok=True)
                destination_file = os.path.join(destination_path,
                                                os.path.basename(source_file))
            else:
                if not os.path.exists(destination_path):
                    destination_file = destination_path
                    destination_path = os.path.dirname(destination_path)
                    os.makedirs(destination_path, exist_ok=True)
                else:
                    print("Such a directory has already exsists")
        else:
            print("Error: Operation should be 'mv'")
    else:
        print("Error: Invalid command format."
              "Please use 'mv source_file destination_path'.")
    try:
        os.rename(source_file, destination_file)
    except Exception as e:
        print(e)
