import os


def _check_path(new_path: str) -> None:
    # helper function to traverse and check path to new file
    # new directory is created if one was not found

    cur_path = ""
    for directory in new_path.split("/"):
        cur_path = os.path.join(cur_path, directory)
        if not os.path.exists(cur_path):
            os.mkdir(cur_path)


def move_file(command: str) -> None:
    operation, old_file_loc, new_file_loc = command.split()
    if operation == "mv" and old_file_loc != new_file_loc:
        # checking if there is any intermediate directory in new file location
        if "/" in new_file_loc:
            # separating path from actual file name
            new_path, *_ = new_file_loc.rsplit("/", 1)

            # checking the case when new file location is only a path
            # if such case new file name should be the same as the oldfile name
            if new_file_loc.endswith("/"):
                # checking for intermediate directories in old file location
                # if such case we separate filename - we will need only it
                if "/" in old_file_loc:
                    _, old_file_name = old_file_loc.rsplit("/", 1)
                    new_file_loc = new_path + "/" + old_file_name
                else:
                    new_file_loc = new_path + "/" + old_file_loc

            # helper function to check the path to new file
            _check_path(new_path)

        with open(old_file_loc) as reader, open(new_file_loc, "w") as writer:
            writer.write(reader.read())

        os.remove(old_file_loc)
