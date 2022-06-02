import os


def move_file(command: str):
    cmd = command.split()

    if "/" in cmd[-1]:
        path = cmd[-1].split("/")[:-1]
        folder_name = f"{path[0]}"

        for i in range(len(path)):
            os.mkdir(folder_name)
            if i < len(path) - 1:
                folder_name += f"/{path[i + 1]}"

        path_to_new_file = f"{folder_name}/{cmd[-1].split('/')[-1]}"

    else:
        path_to_new_file = cmd[-1]

    with open(path_to_new_file, "w") as new_f, open(cmd[1], "r") as old_f:
        new_f.write(old_f.read())

    os.remove(cmd[1])
