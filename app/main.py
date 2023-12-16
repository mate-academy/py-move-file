import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        operation, source_file, destination_path = command.split()
        if operation == "mv":
            if not os.path.dirname(destination_path):
                os.replace(source_file, destination_path)
            elif destination_path.endswith("/"):
                os.makedirs(destination_path, exist_ok=True)
                os.replace(source_file, os.path.join(destination_path,
                                                     source_file))
            else:
                destination_file = destination_path
                destination_path = os.path.dirname(destination_path)
                os.makedirs(destination_path, exist_ok=True)
                os.rename(source_file, destination_file)
        else:
            print("Error: command should by `mv source_file destination_path`")
    else:
        print("Error: wrong format")
