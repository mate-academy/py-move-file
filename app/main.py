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
        if "/" in new_file_loc:
            new_path, *_ = new_file_loc.rsplit("/", 1)
            if new_file_loc.endswith("/"):
                if "/" in old_file_loc:
                    _, old_file_name = old_file_loc.rsplit("/", 1)
                    new_file_loc = new_path + "/" + old_file_name
                else:
                    new_file_loc = new_path + "/" + old_file_loc

            _check_path(new_path)

        with open(old_file_loc) as reader, open(new_file_loc, "w") as writer:
            writer.write(reader.read())
        os.remove(old_file_loc)
