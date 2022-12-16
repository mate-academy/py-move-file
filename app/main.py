import os


class CommandError(Exception):
    pass


def move_file(command: str) -> None:
    action, old_file, road_to_new_file = command.split()
    if action != "mv":
        raise CommandError("Wrong command!")

    start_dir = os.getcwd()

    *to_file, new_file_name = road_to_new_file.split("/")
    new_path = ""

    for direct in to_file:
        new_path = os.path.join(new_path, direct)
        os.mkdir(new_path)
    os.chdir(new_path)

    with open(old_file, "r") as file_to_remove, \
            open(new_file_name, "a") as file_to_add:
        for line in file_to_remove:
            file_to_add.write(line)
        os.chdir(start_dir)
        os.remove(old_file)
