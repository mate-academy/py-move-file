import os


def move_file(command: str) -> None:
    mv, old_filename, new_filename = command.split()

    if mv != "mv":
        return

    splited_new_filename = new_filename.split("/")
    if len(splited_new_filename) == 1:
        os.rename(old_filename, new_filename)
        return

    dirs = splited_new_filename[:-1]
    with open(old_filename, "r") as old_file:
        old_file_content = old_file.read()
        previous = ""
        for i, directory in enumerate(dirs):
            if i != 0:
                directory = previous + "/" + directory
            os.makedirs(directory, exist_ok=True)
            previous = directory
        with open(new_filename, "w") as new_file:
            new_file.write(old_file_content)
    os.remove(old_filename)
