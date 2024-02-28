import os


def move_file(command: str) -> None:
    mv, file, path_to = command.split()

    if mv == "mv":
        part_of_path = os.path.split(path_to)
        if part_of_path[0]:
            os.makedirs(part_of_path[0], exist_ok=True)
        with (
            open(file, "r") as file_in,
            open(path_to, "w") as file_out
        ):
            file_out.write(file_in.read())

        os.remove(file)
