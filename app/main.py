import os


def move_file(command: str) -> None:
    if not command.startswith("mv"):
        return
    args = command.split()
    file_start = args[1]
    new_file = args[2]

    if new_file.endswith("/"):
        new_file_dir = new_file
        destination_file = os.path.join(new_file_dir,
                                        os.path.basename(file_start))
    else:
        new_file_dir, destination_file = os.path.split(new_file)

    if new_file_dir and not os.path.exists(new_file_dir):
        os.makedirs(new_file_dir)

    os.rename(file_start, os.path.join(new_file_dir, destination_file))
