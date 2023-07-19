import os


def move_file(command: str) -> None:
    cmd, source_path, destination_path = command.split()
    new_file_path = os.path.join(*os.path.split(destination_path)[:-1])

    if cmd != "mv":
        raise ValueError('Invalid command. Only "mv" command is supported.')

    if source_path == destination_path:
        print("Source file and destination file have the same name. "
              "No action needed.")
        return

    if new_file_path and not os.path.exists(new_file_path):
        os.makedirs(new_file_path, exist_ok=True)

    os.rename(source_path, destination_path)
