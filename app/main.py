import os


def move_file(command: str) -> None:
    command, file_name, location = command.split()

    if "/" not in location and file_name != location:
        os.rename(file_name, location)
        return

    if not os.path.isfile(location):
        directories = location[:location.rfind("/")]
        os.makedirs(directories, exist_ok=True)

        with open(file_name) as file_in, open(location, "w") as file_out:
            file_out.write(file_in.read())

        os.remove(file_name)
