import os


def move_file(command: str) -> None:
    instruction, in_file_name, new_file_destination = command.split()
    new_file_path = os.path.dirname(new_file_destination)
    if os.path.exists(in_file_name) and instruction == "mv":
        if "/" in new_file_destination:
            os.makedirs(new_file_path, exist_ok=True)
        with (open(in_file_name, "r") as in_file,
              open(new_file_destination, "w") as new_file):
            new_file.write(in_file.read())
        os.remove(in_file_name)
