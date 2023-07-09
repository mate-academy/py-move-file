import os


def move_file(command: str) -> None:
    commands = command.split()

    if any([
        len(commands) != 3,
        not command.startswith("mv"),
        command.endswith("/")
    ]):
        return None

    command, old_file, new_file = commands

    if new_file.find("/") != -1:
        new_file_path_list = new_file.split("/")
        directory_path = os.path.join(os.getcwd(), *new_file_path_list[:-1])
        new_file = os.path.join(os.getcwd(), *new_file_path_list)

        os.makedirs(
            directory_path,
            exist_ok=True
        )
    with open(old_file, "r") as in_file, open(new_file, "w") as out_file:
        content = in_file.read()
        out_file = out_file.write(content)

    os.remove(old_file)
