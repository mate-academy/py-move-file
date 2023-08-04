import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command, old_file, new_file = command.split()
        with open(old_file, "r") as o_file:
            content = o_file.read()
        os.remove(old_file)
        new_file_path = os.path.dirname(new_file)
        if new_file_path != "":
            new_file_name = os.path.basename(new_file)
            try:
                os.makedirs(new_file_path)
            except FileExistsError:
                pass
            finally:
                with open(str(new_file_path + "/" + new_file_name), "w")\
                        as n_file:
                    n_file.write(content)
        else:
            with open(new_file, "w") as new_file:
                new_file.write(content)
