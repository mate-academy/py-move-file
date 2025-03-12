import os


def move_file(command: str) -> None:
    result = command.split(" ")
    if result[0] == "mv":
        directory = result[-1].split("/")
        name_future_file = directory[-1]
        path_creating_file = os.path.abspath(f"{result[1]}")
        if len(directory) > 1:
            path_for_mkdir = "/".join(directory[:len(directory) - 1])
            if not os.path.isdir(path_for_mkdir):
                try:
                    os.makedirs(path_for_mkdir)
                except OSError:
                    pass
            named_directory = os.path.join(path_for_mkdir, name_future_file)
            with (open(path_creating_file, "r") as file_read,
                  open(named_directory, "w") as file_write):
                file_write.write(file_read.read())
            os.remove(path_creating_file)
        else:
            with (open(path_creating_file, "r") as file_read,
                  open(name_future_file, "w") as file_write):
                file_write.write(file_read.read())
            os.remove(path_creating_file)
    else:
        return
# path_creating_file = os.path.abspath("file.txt")
# with open(path_creating_file, "r") as file:
#     file.read()

# print(move_file("mv file.txt first_dir/second_dir/third_dir/file2.txt"))
