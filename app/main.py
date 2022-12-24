import os


def move_file(command: str) -> None:
    files = command.split()
    with open(files[1], "r") as old_file:
        if files[0] == "mv":
            move_to = files[2].split("/")
            path = ""
            for folder in move_to:
                if folder != move_to[-1]:
                    path = os.path.join(path, folder)
                    os.mkdir(path)
            with open(files[2], "w") as new_file:
                new_file.write(old_file.read())
                os.remove(files[1])
