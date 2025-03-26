import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError("Command should contains 3 elements "
                         "separated by a space")
    elif command.split()[0] != "mv":
        raise ValueError("First element should be \'mv\'")

    command = command.split()
    file_name = command[1]
    destination = command[2]

    if "/" not in destination:
        os.rename(file_name, destination)
    else:
        directory = os.path.dirname(destination)
        os.makedirs(os.path.join(os.getcwd(), directory), exist_ok=True)

        new_file_path = os.path.join(os.getcwd(), destination)

        with open(file_name, "r") as old_file:
            with open(new_file_path, "w") as new_file:
                new_file.write(old_file.read())
        os.remove(file_name)
