import os


def move_file(command: str) -> str | None:

    split_command = command.split()
    if len(split_command) != 3:
        print(
            "Invalid command format. Make sure"
            " it is \'command file_path destination_path\'"
        )
        return

    if split_command[0] != "mv":
        print("Incorrect command. Make sure you used valid command")
        return

    source = split_command[1]
    destination = split_command[2]
    destination_dir = os.path.dirname(destination)

    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    os.rename(source, destination)
