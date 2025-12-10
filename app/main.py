import os


def move_file(command: str) -> None:
    file_names = command.split()
    if len(file_names) != 3 or file_names[0] != "mv":
        return
    source_file = file_names[1]
    destination_path = file_names[2]
    if destination_path.endswith(os.sep) or os.path.isdir(destination_path):
        destination_path = os.path.join(
            destination_path, os.path.basename(source_file))
    normalized_path = os.path.normpath(destination_path)
    path_parts = normalized_path.split(os.sep)
    current_path = ""
    for part in path_parts[:-1]:
        current_path = os.path.join(current_path, part)
        try:
            os.mkdir(current_path)
        except FileExistsError:
            pass
    try:
        with (open(file_names[1], "r")
              as file_in, open(destination_path, "w") as file_out):
            file_out.write(file_in.read())
        os.remove(source_file)
    except OSError:
        return


if __name__ == "__main__":
    move_file("mv file.txt first_dir/second_dir/third_dir/file2.txt")
