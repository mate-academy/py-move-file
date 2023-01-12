import os.path


def move_file(command: str) -> None:
    new_f = os.path.split(command)[1]
    mv, source_f, directories_new = command.split()
    directories = directories_new.replace(new_f, "")
    first, second, quotes = directories.split("/")
    if os.path.exists(first):
        os.mkdir("first/second")
    else:
        os.mkdir("first")
        os.mkdir("first/second")
    with open(source_f, "r") as source, open(new_f, "w") as new:
        new.write(source.read())
    os.remove(source_f)
