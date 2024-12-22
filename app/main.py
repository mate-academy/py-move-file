import os


def move_file(command: str) -> None:
    command_list = command.split()
    path = ""

    try:
        if not isinstance(command, str):
            raise TypeError("Command must be string")
        if command[:2] != "mv":
            raise ValueError("Command must start with keyword 'mv'")
        if len(command_list) != 3:
            raise ValueError(
                "Command must include 'mv', source file name and new file name"
            )
    except (TypeError, ValueError) as e:
        print(e)
        return

    try:
        if "/" in command_list[2]:
            path_list = command_list[2].split("/")[:-1]

            for directory in path_list:
                path = os.path.join(path, directory)
                try:
                    os.mkdir(path)
                except FileExistsError:
                    continue

            with (
                open(
                    command_list[1], "r"
                ) as old_file,
                open(
                    f"{path}/{command_list[2].split("/")[-1]}", "w"
                ) as new_file
            ):
                new_file.write(old_file.read())
        else:
            with (
                open(
                    command_list[1], "r"
                ) as old_file,
                open(
                    f"{command_list[2].split("/")[-1]}", "w"
                ) as new_file
            ):
                new_file.write(old_file.read())

        os.remove(command_list[1])
    except FileNotFoundError:
        print("The file was not found")
        return
