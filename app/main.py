import os


def move_file(command: str) -> None:
    old_file = command.split(" ")[1]
    new_file = command.split(" ")[2]

    new_path = "/".join(new_file.split("/")[:-1])
    if len(new_path) != 0:
        os.makedirs(new_path, exist_ok=True)

    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())
    os.remove(old_file)
