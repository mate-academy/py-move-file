import os


def move_file(command: str) -> None:
    cmd = command.split()
    if "mv" in cmd and len(cmd) == 3:
        path = cmd[cmd.index("mv") + 1:]
        old_file = path[0]
        if "/" in path[1]:
            directories = path[1].split("/")[:-1]
            dirs_path = os.path.join(*directories)
            os.makedirs(dirs_path, exist_ok=True)
            new_file = os.path.join(
                dirs_path,
                path[1].split("/")[-1]
            )
        else:
            new_file = path[1]

        with open(old_file) as file_out, open(new_file, "w") as file_in:
            file_in.write(file_out.read())

        os.remove(old_file)
