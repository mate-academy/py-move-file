import os


def move_file(command: str) -> None:
    try:
        command, file_to_move, path = command.split()
        folders = path.split("/")
        new_file_name = folders.pop(-1)
        current_folder = os.getcwd()

        if command != "mv":
            raise ValueError("Incorrect command")

        destination_path = os.path.join(current_folder, *folders)
        os.makedirs(destination_path, exist_ok=True)
        destination_path = os.path.join(destination_path, new_file_name)
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
