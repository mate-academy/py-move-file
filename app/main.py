import os


def move_file(command: str) -> None:
    if len(command.split()) != 3 or command.split()[0] != "mv":
        return None

    _, source, our_new_file_path = command.split()
    dir_path = os.path.dirname(our_new_file_path)
    file_name = os.path.basename(our_new_file_path)

    if not file_name or os.path.isdir(our_new_file_path):
        file_name = os.path.basename(source)
        our_new_file_path = os.path.join(our_new_file_path, file_name)
        dir_path = os.path.dirname(our_new_file_path)

    if dir_path:
        parts = dir_path.split("/")
        for i in range(len(parts)):
            path = "/".join(parts[:i + 1])
            if not os.path.isdir(path):
                os.mkdir(path)

    with (open(source, "r") as old_file,
          open(our_new_file_path, "w") as new_file):
        new_file.write(old_file.read())
    os.remove(source)
