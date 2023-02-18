import os


def move_file(command: str) -> None:
    try:
        command, file_to_move, path = command.split()
        folders = path.split("/")
        new_file_name = folders.pop(-1)
        source_folder = ""

        if command != "mv":
            raise ValueError("Incorrect command")

        for folder in folders:
            destination_path = os.path.join(source_folder, folder)
            source_folder = destination_path
            if not os.path.exists(destination_path):
                os.mkdir(destination_path)

        destination_path = os.path.join(source_folder, new_file_name)
        with (
            open(file_to_move, "r") as file_to_move,
            open(destination_path, "w") as new_file
        ):
            new_file.write(file_to_move.read())
        os.remove(file_to_move.name)

    except FileNotFoundError as error:
        print(error)
    except ValueError as error:
        print(error)
