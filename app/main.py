import os


class CommandError(Exception):
    pass


def move_file(command: str) -> None:
    command = command.split()
    if len(command) != 3:
        raise CommandError(f"Wrong format of command: {command}")

    if command[0] != "mv":
        raise CommandError(f"Wrong command:"
                           f"'{command[0]}', did you mean 'mv'?")

    file_name, full_path = command[1], command[2]
    only_path = os.path.split(full_path)[0]
    if only_path:
        os.makedirs(only_path, exist_ok=True)
    with (open(file_name, "r") as source, open(full_path, "w") as write_file):
        write_file.write(source.read())
    os.remove(file_name)
