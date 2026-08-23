import os


def move_file(command: str) -> None:
    command_ls = command.split()
    if len(command_ls) == 3 and command_ls[0] == "mv":
        parts = command_ls[2].split("/")
        old_file_name, path, new_file_name = (
            command_ls[1],
            parts[0:-1],
            parts[-1])
        if new_file_name == "":
            new_file_name = old_file_name
        current_path = ""
        for directory in path:
            current_path = os.path.join(current_path, directory)
            if not os.path.exists(current_path):
                os.mkdir(current_path)
        with open(old_file_name) as source_file:
            content = source_file.read()
        with open(os.path.join(*path, new_file_name), "w") as new_file:
            new_file.write(content)
        os.remove(old_file_name)
