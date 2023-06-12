from os import path, makedirs, remove


def move_file(command: str) -> None:
    try:
        cmd_name, file_path, new_file_path = command.split(" ")
        if cmd_name != "mv":
            raise ValueError("Incorrect command!!! "
                             "Must be: mv path_to_file new_path")
        if not path.exists(file_path):
            raise FileNotFoundError("File doesn't exist!!!")
        dirs = path.dirname(new_file_path)
        if dirs:
            makedirs(dirs, exist_ok=True)
        with (open(file_path, "r") as old_file,
              open(new_file_path, "w") as new_file):
            new_file.write(old_file.read())
        remove(file_path)
    except (ValueError, FileNotFoundError) as error:
        print(error)
