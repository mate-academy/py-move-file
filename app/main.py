import os


def move_file(command: str) -> None:
    command_parts = command.split()
    mv, file_name, destination = command_parts

    if len(command_parts) != 3:
        raise ValueError("Command should contains 3 elements "
                         "separated by a space")
    elif mv != "mv":
        raise ValueError("First element should be \'mv\'")

    if "/" not in destination:
        os.rename(file_name, destination)
    else:
        directory = os.path.dirname(destination)
        os.makedirs(os.path.join(os.getcwd(), directory), exist_ok=True)

        new_file_path = destination

        with open(file_name, "r") as old_file:
            with open(new_file_path, "w") as new_file:
                new_file.write(old_file.read())
        os.remove(file_name)
