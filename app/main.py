import os


def move_file(command: str) -> None:
    command, file_name, file_copy = command.split(" ")

    if command == "mv" and file_copy[-1] != "\\":
        with open(file_name, "r") as file:
            file_content = file.read()
        os.remove(file_name)

        file_copy_source = file_copy.split("/")
        file_copy_name = file_copy_source.pop(-1)

        path = ""
        for source in file_copy_source:
            path = os.path.join(path, source)
            os.makedirs(path, exist_ok=True)

        with open(os.path.join(path, file_copy_name), "w") as file_copy:
            file_copy.write(file_content)
