import os


def move_file(command: str) -> None:
    try:
        cmd, source_file, destination_path = command.split()
    except ValueError:
        return
    if cmd != "mv":
        return
    if destination_path.endswith(os.sep) or os.path.isdir(destination_path):
        destination_path = os.path.join(
            destination_path, os.path.basename(source_file))
    parent_dir = os.path.dirname(destination_path)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)
    try:
        with (open(source_file, "r")
              as file_in, open(destination_path, "w") as file_out):
            file_out.write(file_in.read())
        os.remove(source_file)
    except OSError:
        return


if __name__ == "__main__":
    move_file("mv fileNEW.txt first_dir/second_dir/third_dir/file2.txt")
