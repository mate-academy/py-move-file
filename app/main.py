import os


def move_file(command: str) -> None:
    file_names = command.split()
    if len(file_names) != 3 or file_names[0] != "mv":
        return
    if file_names[2].endswith("/"):
        return
    path = file_names[2].split("/")
    current_path = ""
    for part in path[:-1]:
        current_path += part + "/"
        try:
            os.mkdir(current_path)
        except FileExistsError:
            pass
    try:
        with (open(file_names[1], "r")
              as file_in, open(file_names[2], "w") as file_out):
            file_out.write(file_in.read())
        os.remove(file_names[1])
    except OSError:
        return


if __name__ == "__main__":
    move_file("mv file.txt first_dir/second_dir/third_dir/file2.txt")
