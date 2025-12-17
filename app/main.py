import os


def move_file(command: str) -> None:
    list_command = command.split(" ")

    try:
        new_file = list_command[2]
        old_file = list_command[1]
        try:
            if "/" in new_file:
                list_new_file = new_file.split("/")
                path = os.path.join(*list_new_file)
                os.makedirs(os.path.dirname(path), exist_ok=True)
            elif "\\" in new_file:
                list_new_file = new_file.split("\\")
                path = os.path.join(*list_new_file)
                os.makedirs(os.path.dirname(path), exist_ok=True)
            else:
                path = new_file

            with open(old_file, "r") as old, open(path, "w") as new:
                new.write(old.read())
                os.remove(old_file)
        except FileNotFoundError:
            pass
    except IndexError:
        pass
