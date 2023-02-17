import os


def move_file(command: str) -> None:
    cm, first_file, second_file = command.split()
    if cm == "mv" and first_file != second_file:
        directory = second_file.split("/")
        path = directory[0]
        os.makedirs(path, exist_ok=True)
        for i in range(1, len(directory) - 1):
            path += "/" + directory[i]
            os.makedirs(path, exist_ok=True)

        with (
            open(first_file, "r") as file_remove,
            open(second_file, "w") as file_create
        ):
            file_create.write(file_remove.read())

        os.remove(first_file)
