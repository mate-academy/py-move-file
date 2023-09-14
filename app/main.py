import os.path


def move_file(command: str) -> None:

    if len(command.split()) != 3:
        raise ValueError("Incorrect command")

    cmd, file, new_file = command.split()
    if cmd != "mv":
        raise ValueError("Incorrect command")

    destination, file_name = os.path.split(new_file)

    if destination:
        os.makedirs(destination, exist_ok=True)

        with open(file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
        os.remove(file)
    else:
        os.rename(file, new_file)
