from os import remove, mkdir, rename, path


def move_file(command: str) -> None:
    separated = command.split(" ")

    if len(separated) != 3:
        return

    com, source, destination = separated

    directories = destination.split("/")

    if com != "mv":
        return

    if len(directories) == 1:
        rename(source, destination)
        return

    directory = ""
    for direct in directories[0:-1]:

        directory = path.join(directory, direct)
        try:
            mkdir(directory)

        except FileExistsError:
            continue
    filename = directories[-1]

    with (open(source, "r") as file,
          open(path.join(directory, filename), "w") as outfile):

        opened_file = file.read()

        outfile.write(opened_file)

    remove(source)
