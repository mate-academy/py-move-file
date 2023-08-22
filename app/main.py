import os


def move_file(command: str) -> None:
    try:
        mv_command, old_file, new_file = command.split()
    except ValueError:
        raise Exception("Enter correct command!")

    if old_file != new_file and mv_command == "mv":
        dir_path = os.path.dirname(new_file)
        if dir_path and not os.path.exists(dir_path):
            dirs = dir_path.split("/")
            dir_ = ""
            for temp in dirs:
                dir_ = os.path.join(dir_, temp)
                if not os.path.exists(dir_):
                    os.mkdir(dir_)

        with open(old_file) as file_in, open(new_file, "w") as file_out:
            file_content = file_in.read()
            file_out.write(file_content)

        os.remove(old_file)
