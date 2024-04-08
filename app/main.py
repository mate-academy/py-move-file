import os


def move_file(command: str) -> None:
    _, file_source, path_another_file = command.split()
    folders = path_another_file.split("/")
    curr_folder = ""

    if file_source == path_another_file:
        return

    if len(folders) == 1:
        os.rename(file_source, path_another_file)
        return

    for folder in folders:
        if "." in folder:
            break
        curr_folder += f"{folder}/"
        if not os.path.exists(curr_folder):
            os.mkdir(curr_folder)

    with (
        open(file_source, "r") as source,
        open(os.path.join(*folders), "w") as moved
    ):
        moved.write(source.read())
    os.remove(file_source)
