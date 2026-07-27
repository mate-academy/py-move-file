import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, file_from, file_to = parts

    if file_to.endswith("/"):
        file_to += file_from.split("/")[-1]

    dirs = file_to.split("/")[:-1]

    current_path = ""
    for folder in dirs:
        if current_path == "":
            current_path = folder
        else:
            current_path = current_path + "/" + folder

        if not os.path.exists(current_path):
            os.mkdir(current_path)

    with (
        open(file_from, "r") as f_in,
        open(file_to, "w") as f_out,
    ):
        f_out.write(f_in.read())

    os.remove(file_from)
