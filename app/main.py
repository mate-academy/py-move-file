import os


def move_file(file_names: str) -> None:
    names = file_names.split()
    if names[0] != "mv" or names[1] == names[2]:
        return
    if "/" in names[2]:
        os.makedirs(os.path.dirname(names[2]), exist_ok=True)
    with open(names[1], "r") as file_in, open(names[2], "w") as file_out:
        file_out.writelines(file_in.read())
    os.remove(names[1])
