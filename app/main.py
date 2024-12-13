import os


def extract_path(whole_path: str) -> str:
    if "/" in whole_path:
        index = whole_path.rfind("/")
        return whole_path[:index]

    return ""


def create_dirs(new_path: str) -> None:
    directories = ""

    for directory in new_path.split("/"):
        directories += directory + "/"

        if not os.path.exists(directories):
            os.mkdir(directories)


def move_file(command: str) -> None:
    command = command.split(" ")

    source_file = command[1]
    new_file = command[2]

    source_path = extract_path(source_file)
    new_path = extract_path(new_file)

    if source_path != new_path:
        create_dirs(new_path)

    with (open(source_file, "r") as source_f, open(new_file, "w") as new_f):
        new_f.write(source_f.read())

    os.remove(source_file)
