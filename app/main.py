import os


def move_file(command: str) -> None:

    _, file_name, copy_path = command.split()
    copy_path = copy_path.split("/")

    if copy_path[:-1]:
        os.makedirs(os.path.join(
            *copy_path[:-1]
        ), exist_ok=True)

    with (open(file_name, "r") as file,
          open(os.path.join(*copy_path), "w") as copy):
        copy.write(file.read())
    os.remove(file_name)
