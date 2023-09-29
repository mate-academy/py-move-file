import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) == 3 and command[0] == "mv":
        origin_file, new_file = command[1:]
        first_part, second_part = os.path.split(new_file)
        if first_part:
            os.makedirs(first_part, exist_ok=True)
            with (open(origin_file, "r") as file_from,
                  open(new_file, "w") as file_to):
                file_to.write(file_from.read())
            os.remove(file_from.name)
        else:
            os.rename(origin_file, new_file)
