import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "mv":
        _, current_file, new_file = parts
        if new_file.endswith("/"):
            os.makedirs(new_file, exist_ok=True)
            new_file = os.path.join(new_file, os.path.basename(current_file))
        else:
            dir_name, file_to_copy = os.path.split(new_file)
            if len(dir_name) > 0:
                os.makedirs(dir_name, exist_ok=True)
        with (open(current_file, "r") as file_in,
              open(new_file, "w") as file_out):
            file_out.write(file_in.read())
        os.remove(current_file)
