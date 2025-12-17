import os


def move_file(command: str) -> None:
    list_command = command.split(" ")
    if list_command[0] == "mv" and len(list_command) == 3:
        mv, old_file, new_file = list_command
        try:
            dir_path = os.path.dirname(new_file)
            file_name = os.path.basename(new_file)
            if dir_path:
                os.makedirs(dir_path, exist_ok=True)
            if not file_name:
                new_file = os.path.dirname(new_file) + "/" + old_file
            with open(old_file, "r") as old, open(new_file, "w") as new:
                new.write(old.read())
                os.remove(old_file)
        except FileNotFoundError:
            pass
