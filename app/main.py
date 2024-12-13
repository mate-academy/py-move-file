import os


def move_file(command: str) -> None:
    action, old_file, road_to_new_file = command.split()
    if action != "mv":
        raise Exception("Wrong command")

    root_directory = os.getcwd()

    to_file, new_file = road_to_new_file.split("/")
    new_path = ""

    for direction in to_file:
        new_path = os.path.join(new_file, direction)
        os.mkdir(new_path)
    os.chdir(new_path)

    with open(old_file, "r") as file_to_remove, \
            open(new_file, "a") as file_to_add:
        for line in file_to_remove:
            file_to_add.write(line)
        os.chdir(root_directory)
        os.remove(old_file)
