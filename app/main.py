import os


def move_file(command: str) -> None:
    list_commands = command.split()

    if len(list_commands) == 3 and list_commands[0] == "mv":
        source_file = list_commands[1]
        destination_file = list_commands[2]

        destination_dir = os.path.dirname(destination_file)
        file_name = os.path.basename(destination_file)

        if destination_dir and not os.path.exists(destination_dir):
            os.makedirs(destination_dir, exist_ok=True)

        os.rename(source_file, os.path.join(destination_dir, file_name))
