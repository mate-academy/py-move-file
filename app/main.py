import os


def move_file(command: str = "mv file.txt some_dir/new_file.txt") -> None:
    file, dest = command.split()[1:]
    orig_dir = os.getcwd()
    if not os.path.exists(file):
        with open(file, "w") as file_:
            file_.write("")
    with open(file, "r") as inp_file:
        orig_file = inp_file.read()
    way = None
    to_file = dest
    if "/" in dest:
        dest = dest.split("/")
        to_file = dest[-1]
        way = dest[:-1]
    if way:
        for folder in way:
            if os.path.exists(folder):
                os.chdir(folder)
            else:
                os.mkdir(folder)
                os.chdir(folder)
    with open(to_file, "w") as new_file:
        new_file.write(orig_file)
    os.chdir(orig_dir)
    os.remove(f"./{file}")


if __name__ == "__main__":
    pass
