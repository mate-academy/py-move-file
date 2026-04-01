import os


def move_file(command: str) -> None:
    comm, old_file, new_file = command.split()
    if comm == "mv":
        dir_file = new_file.split("/")
        for index in range(1, len(dir_file)):
            try:
                os.mkdir("/".join(dir_file[:index]))
            except FileExistsError:
                print("You already have this directory")

        with open(old_file, "r") as file_in, open(new_file, "w") as file_on:
            file_on.write(file_in.read())

        os.remove(old_file)
