import os


def move_file(command: str) -> None:
    action, file_name, path = command.split()
    if action == "mv":
        with open(file_name) as file_to_read:

            # check if directories are in path for writing file
            if "/" in path or "\\" in path:
                path_normalized = path.replace("\\", "/")
                dirs = path_normalized.split("/")
                cur_path = os.getcwd()

                # creating non-existing folder
                # and appending their names to cur_path
                for folder in dirs[:-1]:
                    if not os.path.isdir(os.path.join(cur_path, folder)):
                        os.mkdir(os.path.join(cur_path, folder))
                    cur_path = os.path.join(cur_path, folder)

                # write to file in created directories tree
                with (open(os.path.join(cur_path, dirs[-1]), "w") as
                      file_to_write):
                    file_to_write.write(file_to_read.read())

            # write to file from current directory
            else:
                with open(path, "w") as file_to_write:
                    file_to_write.write(file_to_read.read())
        os.remove(file_name)
