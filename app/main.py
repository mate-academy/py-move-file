import os


def move_file(command: str) -> None:
    """ That will move a file from one location to another """
    # Ex: mv file.txt first_dir/second_dir/third_dir/file2.txt

    (cmd,
     file_in,
     file_out) = command.split(" ")

    if cmd != "mv":
        raise ValueError("Command mv not found")

    if "/" in file_out:
        dir_path = ""
        directories, filename = os.path.split(file_out)

        for directory in directories.split("/"):
            dir_path = os.path.join(dir_path, directory)
            os.makedirs(dir_path, exist_ok=True)

    with open(file_in, "r") as f_in, open(file_out, "w") as f_out:
        f_out.write(f_in.read())

    try:
        os.remove(file_in)
    except OSError as e:
        print(f"We got Error: {e}")
