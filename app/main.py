from os import makedirs, remove, rename


def move_file(command: str) -> None:
    com, old_filename, path_and_new_filename = command.split()
    new_filename = path_and_new_filename.split("/")[-1]
    full_path = ""
    for path in path_and_new_filename.split("/")[:-1]:
        full_path += (path + "/")

    if com != "mv":
        return

    if path_and_new_filename == new_filename:
        rename(old_filename, new_filename)
        return

    try:
        makedirs(full_path)
    except FileExistsError as e:
        print(e)

    with (open(old_filename, "r") as old_file,
          open(path_and_new_filename, "w") as new_file):
        new_file.write(old_file.read())
    remove(old_filename)
