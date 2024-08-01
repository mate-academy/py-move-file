from os import mkdir, remove, path


def move_file(command: str) -> None:
    command_line = command.split()
    if len(command_line) == 3 and command_line[0] == "mv":
        new_path = command_line[2].split("/")
        old_path = command_line[1].split("/")
        if new_path[0: -1] != old_path[0: -1]:
            current_path = new_path[0]
            for i in range(len(new_path) - 1):
                if not path.isdir(current_path):
                    mkdir(current_path + "/")
                current_path += "/" + new_path[i + 1]
        with open(command_line[1]) as original_file:
            original_data = original_file.read()
        with open(command_line[2], "w") as copy_file:
            copy_file.write(original_data)
        remove(command_line[1])
