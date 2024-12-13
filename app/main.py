from os import mkdir, remove


def move_file(command: str) -> None:
    command = command.split()
    original_file_name = command[1]

    with open(original_file_name, "r") as file:
        data = file.read()

    path = ''
    for folder in command[2].split('/')[:-1]:
        path += f"{folder}/"
        mkdir(path)

    with open(f"{command[-1]}", "w") as copied_file:
        copied_file.write(data)

    remove(original_file_name)
