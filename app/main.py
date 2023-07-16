from os import makedirs, remove


def move_file(command: str) -> None:
    if len(command.split()) == 3 and command.split()[0] == "mv":
        command, filename, new_file_path = command.split()

        if len(new_file_path.split("/")) > 1:
            makedirs("/".join(new_file_path.split())[:-1], exist_ok=True)

        with (
            open(filename, "r") as file_out,
            open(new_file_path, "w") as file_in
        ):
            file_in.write(file_out.read())

        remove(filename)

    else:
        print("Command is invalid!")
