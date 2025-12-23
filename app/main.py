import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) != 3 or command[0] != "mv":
        raise Exception("Invalid command!")

    _, source_file_name, new_file_path = command
    if not os.path.isfile(source_file_name):
        raise Exception(f"File {source_file_name} does not exist")

    new_file_path = new_file_path.split("/")

    for i in range(1, len(new_file_path)):
        try:
            os.mkdir(os.path.join(*new_file_path[:i]))
        except FileExistsError:
            continue

    with (
        open(source_file_name, "r") as source_file,
        open(os.path.join(*new_file_path), "w") as new_file
    ):
        new_file.write(source_file.read())

    os.remove(source_file_name)
