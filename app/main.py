import os.path


def move_file(command: str) -> None:
    command = command.split(" ")
    if len(command) == 3:
        mv, input_file, new_file = command
        if mv == "mv":
            if os.path.dirname(new_file):
                destination_path = os.path.dirname(new_file)
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path, exist_ok=True)
        os.replace(input_file, new_file)
