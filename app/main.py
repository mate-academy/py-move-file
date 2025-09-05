import os.path


def move_file(command: str) -> None:
    commands = command.split()
    start_file = commands[1]
    if commands[2][-1] == "/":
        os.makedirs(commands[2], exist_ok=True)
        file_path = os.path.join(commands[2], os.path.basename(start_file))
        with (open(start_file, "r") as file_in,
              open(file_path, "w") as file_out):
            content = file_in.read()
            file_out.write(content)
        os.remove(start_file)
    elif "/" in commands[2]:
        file_path = commands[2]
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with (open(start_file, "r") as file_in,
              open(file_path, "w") as file_out):
            content = file_in.read()
            file_out.write(content)
        os.remove(start_file)
    else:
        os.rename(start_file, commands[2])
