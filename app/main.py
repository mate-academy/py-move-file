import os


class CommandError(Exception):
    pass


def move_file(command: str) -> None:
    action, old_file, road_to_new_file = command.split()
    if action != "mv":
        raise CommandError('Command have to start with "mv"!')

    os.makedirs(os.path.dirname(road_to_new_file))

    with (
        open(old_file, "r") as file_to_remove,
        open(road_to_new_file, "a") as file_to_add
    ):
        for line in file_to_remove:
            file_to_add.write(line)
        os.remove(old_file)
