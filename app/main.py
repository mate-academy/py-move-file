import os


def move_file(command: str) -> None:
    command = command.split()

    if len(command) == 3 and command[0] == "mv" and command[1] != command[2]:
        with open(command[1], "r") as file_to_delete:
            context = file_to_delete.read()

        destination, new_file_name = os.path.split(command[2])
        if destination:
            os.makedirs(destination, exist_ok=True)

        with open(command[2], "w") as file:
            file.write(context)

        os.remove(command[1])
