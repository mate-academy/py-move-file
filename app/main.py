import os


def move_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) != 3:
        return

    destination_list = command_list[2].split("/")

    if len(destination_list) > 1:
        for index, name in enumerate(destination_list):
            if index < len(destination_list) - 1:
                path = os.path.join(*destination_list[:index + 1])
                if not os.path.exists(path):
                    os.mkdir(path)

    if len(command_list) == 3:
        _, first_file, second_file = command_list

        if second_file.endswith("/"):
            second_file = second_file + os.path.basename(first_file)

        if command_list[0] == "mv" and os.path.exists(first_file):
            with (
                open(first_file, "r") as file,
                open(second_file, "w") as newfile
            ):
                newfile.write(file.read())
                os.remove(first_file)
