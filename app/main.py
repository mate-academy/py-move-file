import os.path


def move_file(command: str) -> None:
    command_in_parts = command.split(" ")
    need_derectory = command_in_parts[2].split("/")
    need_derectory.pop(-1)
    if (
        len(command_in_parts) == 3
        and command_in_parts[0] == "mv"
        and os.path.exists(command_in_parts[1])
    ):
        ex_dir = ""
        for directory in need_derectory:
            ex_dir += directory
            if not os.path.exists(ex_dir):
                os.mkdir(ex_dir)
            ex_dir += "/"
        with (
            open(command_in_parts[2], "w") as new_file,
            open(command_in_parts[1], "r") as old_file
        ):
            new_file.write(old_file.read())
        os.remove(command_in_parts[1])
