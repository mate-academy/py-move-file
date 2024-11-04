import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError(
            "You need to specify the command, "
            "file name and the path where to move the file"
        )

    command, file_name, location = command.split()

    if command != "mv":
        raise ValueError("Only mv command is supported")

    os.makedirs(location[:location.rfind("/")], exist_ok=True)

    with open(file_name) as file_in, open(location, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(file_name)
