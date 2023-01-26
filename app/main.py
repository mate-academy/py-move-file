import os


def move_file(command: str) -> None:
    old_file, new_file = command.split()[1:]
    to_del = old_file
    path = ""

    with open(old_file, "r") as old:
        context = old.read()
        if "/" not in new_file:
            with open(new_file, "w") as new:
                new.write(context)
        else:
            directories = new_file.split("/")[:-1]
            new_file = new_file.split("/")[-1]
            for directory in directories:
                path = os.path.join(path, directory)
                os.mkdir(path)
            with open(f"{path}/{new_file}", "w") as file:
                file.write(context)
    os.remove(to_del)
