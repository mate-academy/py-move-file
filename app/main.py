import os


def move_file(command: str) -> None:
    list_command = command.split(" ")
    if list_command[0] == "mv" and len(list_command) == 3:
        try:
            mv, old_file, new_file = list_command
            try:
                dir_path = os.path.dirname(new_file)
                if dir_path:
                    os.makedirs(dir_path, exist_ok=True)
                else:
                    pass

                with open(old_file, "r") as old, open(new_file, "w") as new:
                    new.write(old.read())
                    os.remove(old_file)
            except FileNotFoundError:
                pass
        except IndexError:
            pass
    else:
        pass
