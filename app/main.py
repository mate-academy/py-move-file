from os import remove, rename, mkdir


def move_file(command: str) -> None:
    command, file1, file2_path = command.split()
    *dirs, file2 = file2_path.split("/")

    if command == "mv":
        if not dirs:
            rename(file1, file2)
            return

        for index in range(len(dirs)):
            mkdir("/".join(dirs[:index + 1]))

        with open(file1, "r") as source, open(file2_path, "w") as copy:
            copy.write(source.read())

        remove(file1)
