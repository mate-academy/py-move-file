import os


def move_file(command: str) -> None:
    command, file_to_move, path = command.split()
    folders = path.split("/")
    source_folder = ""

    if command == "mv":
        for folder in folders:

            if folder[-4:] != ".txt":
                destination_path = os.path.join(source_folder, folder)
                source_folder = destination_path
                if os.path.exists(destination_path) is False:
                    os.mkdir(destination_path)

            if folder[-4:] == ".txt":
                destination_path = os.path.join(source_folder, folder)
                with (
                    open(file_to_move, "r") as file_to_move,
                    open(destination_path, "w") as new_file
                ):
                    new_file.write(file_to_move.read())
                os.remove(file_to_move.name)
