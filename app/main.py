import os


def move_file(command_line: str) -> None:
    command, old_file, new_file = command_line.split(" ")

    if command != "mv":
        return

    if "/" in new_file:
        path = new_file[:new_file.rfind("/")]
        os.makedirs(path, exist_ok=True)
    else:
        os.rename(old_file, new_file)
        return

    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(old_file)


move_file("mv file.txt first_dir/second_dir/third_dir/file2.txt")
