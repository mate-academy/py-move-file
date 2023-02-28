import os


def move_file(command: str) -> None:

    if "/" not in command and len(command.split()) == 3:
        os.rename(command.split()[1], command.split()[2])
        return

    command = command.split()
    if "mv" not in command[0]:
        return

    path_with_file = [path.split("/") for path in command if "/" in path][0]
    copy_file = path_with_file[-1]
    folders = path_with_file[:-1]

    if not os.path.exists(path_with_file[0]):
        os.mkdir(path_with_file[0])
        first_path = path_with_file[0]

        for folder in folders:
            next_path = os.path.join(first_path, folder)
            os.makedirs(next_path)
            first_path = next_path

        with open(command[1], "r") as file_in, \
                open(os.path.join(first_path, copy_file), "w") as file_out:
            file_out.write(file_in.read())
        os.remove(command[1])
