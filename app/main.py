import os


def move_file(command: str) -> None:
    curr_file = command.split()
    if len(curr_file) != 3 and curr_file[0] != "mv":
        return
    old_file, new_file = curr_file[1], curr_file[2]
    if new_file.find("/") != -1:
        path = os.path.join(*new_file[:new_file.rfind("/")].split("/"))
        try:
            os.makedirs(path)
        except FileExistsError:
            with open(old_file) as old, open(new_file, "w") as new:
                new.write(old.read())
    with open(old_file) as old, open(new_file, "w") as new:
        new.write(old.read())
    os.remove(old_file)
