import os


def move_file(command: str) -> None:
    command_parts = command.split(" ")
    if len(command_parts) != 3 or command_parts[0] != "mv":
        raise ValueError("Command is incorrect")
    file_name, new_file_with_path = command_parts[1:]
    path_to_file = os.path.split(new_file_with_path)[0]
    if len(path_to_file) != 0:
        os.makedirs(path_to_file, exist_ok=True)
    with (open(file_name, "r") as file_in,
          open(new_file_with_path, "w") as file_out):
        content = file_in.read()
        file_out.write(content)
    os.remove(file_name)
