import os.path


def move_file(command: str) -> None:
    mv_command = command.split(" ")[0]
    input_file = command.split(" ")[1]
    new_file = command.split(" ")[2]
    if mv_command == "mv":
        if os.path.dirname(new_file):
            destination_path = os.path.dirname(new_file)
            if not os.path.exists(destination_path):
                os.makedirs(destination_path, exist_ok=True)
        os.replace(input_file, new_file)
