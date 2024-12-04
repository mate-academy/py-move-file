import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command, current_file, new_file = command.split()
        dir_name, file_to_copy = os.path.split(new_file)
        if len(dir_name) > 0:
            os.makedirs(dir_name, exist_ok=True)
        with (open(current_file, "r") as file_in,
              open(os.path.join(dir_name, file_to_copy), "w") as file_out):
            file_out.write(file_in.read())
        os.remove(current_file)
