from os import mkdir, remove


def move_file(command: str) -> None:
    command_lst = command.split()

    if command_lst[0] != 'mv':
        return

    old_file = command_lst[1]
    new_file = command_lst[2]

    path = ''
    for folder in new_file.split('/')[:-1]:
        path += f"{folder}/"
        mkdir(path)

    with open(old_file, 'r') as file_origin, open(new_file, 'w') as file_copy:
        file_copy.write(file_origin.read())

    remove(old_file)
