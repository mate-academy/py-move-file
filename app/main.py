from os import makedirs, path, remove


def move_file(command: str) -> None:
    if len(command.split()) == 3 and command.split()[0] == "mv":
        command, filename, new_file_path = command.split()

        directories, _ = path.split(new_file_path)
        if directories:
            makedirs(directories, exist_ok=True)

        with (
            open(filename, "r") as file_out,
            open(new_file_path, "w") as file_in
        ):
            file_in.write(file_out.read())

        remove(filename)

    else:
        print("Command is invalid!")
