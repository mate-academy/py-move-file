import os


def move_file(command: str) -> None:
    """ That will move a file from one location to another """
    # Ex: mv file.txt first_dir/second_dir/third_dir/file2.txt

    cmd, file_in, file_out = command.split(" ")[0], command.split(" ")[1], command.split(" ")[2]

    if cmd != "mv":
        raise ValueError("Command mv not found")

    if "/" in file_out:
        dir_path = ""

        for directory in os.path.dirname(file_out).split("/"):
            dir_path = os.path.join(dir_path, directory)

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

    with open(file_in, "r") as f_in, open(file_out, "w") as f_out:
        f_out.write(f_in.read())

    try:
        os.remove(file_in)
    except OSError as e:
        print(f"We got Error: {e}")


print(open("file.txt").read())
# Some
# Text
move_file("mv file.txt first_dir/second_dir/third_dir/file2.txt")
print(open("first_dir/second_dir/third_dir/file2.txt").read())
# Some
# Text
# open("file.txt")
# FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'