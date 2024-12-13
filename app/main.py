import os


def move_file(command: str) -> None:
    command, file_orig, path = command.split()

    if command == "mv":

        file_copy = os.path.split(path)[-1]
        path = path.replace(file_copy, "")

        if path and not os.path.exists(path):
            os.makedirs(path)
            print("Directory not found. Creating directory")

        with (open(file_orig, "r") as source,
              open(path + file_copy, "a+") as copy):
            copy.write(source.read())
        os.remove(file_orig)
