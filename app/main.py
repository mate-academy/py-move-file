import os


def move_file(command):
    old_file_name = command.split()[1]
    destination_path = command.split()[2]

    if old_file_name.endswith("/") or destination_path.endswith("/"):
        return

    dirs = destination_path.split("/")[:-1]

    dirs_line = ""
    for dir in dirs:
        os.mkdir(dirs_line + dir)
        dirs_line += dir + "/"

    with open(old_file_name, "r") as source_file:
        with open(destination_path, "w") as destination_file:
            destination_file.write(source_file.read())

    os.remove(old_file_name)


move_file("mv file2.txt first_dir/second_dir/third_dir/file.txt")
