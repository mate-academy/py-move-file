from os import makedirs, remove


def move_file(command: str) -> None:
    command, filename, new_file_path = command.split()

    if command == "mv":
        if len(new_file_path.split("/")) > 1:
            makedirs("/".join(new_file_path.split())[:-1])

        with (
            open(filename, "r") as file_out,
            open(new_file_path, "w") as file_in
        ):
            file_in.write(file_out.read())

        remove(filename)

    else:
        print("Command is invalid!")
