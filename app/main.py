import os


def _check_path(new_path: str) -> None:
    cur_path = ""
    for directory in new_path.split("/"):
        cur_path = os.path.join(cur_path, directory)
        if not os.path.exists(cur_path):
            os.mkdir(cur_path)


def move_file(command: str) -> None:
    try:
        operation, old_file_loc, new_file_loc = command.split()
        if not os.path.isfile(old_file_loc):
            raise ValueError
    except ValueError:
        print(
            "Please check the input, "
            "it should be like 'mv file some_dir/new_file'. "
            "The file to move cannot be directory!"
        )
        return
    if operation == "mv" and old_file_loc != new_file_loc:
        if os.path.isdir(new_file_loc):
            new_path, new_file_name = new_file_loc, None
        else:
            new_path, new_file_name = os.path.split(new_file_loc)
            if new_path:
                _check_path(new_path)
        if not new_file_name:
            _, old_file_name = os.path.split(old_file_loc)
            new_file_loc = os.path.join(new_path, old_file_name)

        with open(old_file_loc, "r") as reader:
            with open(new_file_loc, "w") as writer:
                writer.write(reader.read())
        os.remove(old_file_loc)
