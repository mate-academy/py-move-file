import os


def move_file(command: str) -> None:
    list_commands = command.split()

    if len(list_commands) == 3 and list_commands[0] == "mv":
        source_file = list_commands[1]
        destination_file = list_commands[2]

        destination_parts = destination_file.split("/")
        file_name = destination_parts.pop()

        current_path = ""
        for folder in destination_parts:
            current_path = os.path.join(current_path, folder)
            if not os.path.exists(current_path):
                os.mkdir(current_path)

        os.rename(source_file, os.path.join(current_path, file_name))
