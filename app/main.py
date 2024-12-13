import os


def move_file(command: str) -> None:

    separeted_command = command.split()
    if len(separeted_command) != 3:
        raise ValueError("Error in command")
    com, file_name, new_file_name = separeted_command

    if os.path.exists(file_name) and com == "mv":
        if os.path.isdir(new_file_name):
            directory = new_file_name
            update_file_name = os.path.join(new_file_name, file_name)
        else:
            directory = os.path.dirname(new_file_name)
            update_file_name = new_file_name

        if not os.path.exists(new_file_name) and directory:
            os.makedirs(directory, exist_ok=True)

        os.rename(file_name, update_file_name)
