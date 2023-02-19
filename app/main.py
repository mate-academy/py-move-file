import os


def _check_path(new_path: str) -> None:
    # helper function to traverse and check path to new file
    # new directory is created if one was not found

    directories = new_path.split("/")
    path = ""
    for directory in directories:
        path += directory
        if not os.path.exists(path):
            os.mkdir(path)
        path += "/"


def move_file(command: str) -> None:
    operation, old_file_loc, new_file_loc = command.split()
    if operation == "mv" and old_file_loc != new_file_loc:
        # checking if there is any intermediate directories in newfile location
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

            # using helper function to check the path to new file
            _check_path(new_path)

        with open(old_file_loc) as reader, open(new_file_loc, "w") as writer:
            writer.write(reader.read())

        os.remove(old_file_loc)
