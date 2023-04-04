import os


def move_file(command: str) -> None:
    command, file_to_move, new_file = command.split()
    if command == "mv":
        new_file_path = os.path.split(new_file)[0]
        if new_file_path:
            os.makedirs(new_file_path, exist_ok=True)
        with (open(file_to_move, "r") as file_in,
              open(new_file, "w") as file_out):
            content = file_in.read()
            file_out.write(content)
        os.remove(file_to_move)
