import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3 and command_list[0] == "mv":
        file_name = command_list[1]
        path = command_list[2].split("/")
        if command_list[2][-1] == "/":
            path.append(file_name)

        current = ""
        if len(path) > 1:
            for folder in path[:-1]:
                current = os.path.join(current, folder)
                if not os.path.isdir(current):
                    try:
                        os.mkdir(current)
                    except FileExistsError:
                        pass
        current = os.path.join(current, path[-1])

        if os.path.exists(file_name) and file_name != current:
            with (open(file_name, "r") as file_read,
                  open(current, "w") as file_write):
                for line in file_read:
                    file_write.write(line)

            os.remove(file_name)
