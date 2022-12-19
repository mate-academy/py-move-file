import os


def move_file(command: str) -> None:

    source = command.split()[1]
    destination = command.split()[2]

    if source.endswith("/") or destination.endswith("/"):
        return
    files = destination.split("/")[:-1]

    path_line = ""
    for direction in files:
        os.mkdir(path_line + direction)
        path_line += direction + "/"

    with open(source, "r") as file_in, \
            open(destination, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(source)


move_file("mv file.txt first_dir/second_dir/third_dir/file2.txt")
