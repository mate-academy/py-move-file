import os


def move_file(command: str) -> None:

    source, destination = command.split()[1], command.split()[2]

    if source.endswith("/") or destination.endswith("/"):
        return
    files = destination.split("/")[:-1]
    os.makedirs("/".join(files))

    with open(source, "r") as file_in, \
            open(destination, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(source)


move_file("mv file.txt first_dir/second_dir/third_dir/file2.txt")
