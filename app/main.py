import os


def move_file(command: str) -> None:
    command, file_name, location = command.split()

    os.makedirs(location[:location.rfind("/")], exist_ok=True)

    with open(file_name) as file_in, open(location, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(file_name)
