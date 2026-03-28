import os


def move_file(command: str) -> None:
    command_array = command.split(" ")
    if command_array[0] == "mv" and len(command_array) == 3:
        file_to_delete, file_to_move = command_array[1:]
        try:
            with open(file_to_delete, "r") as file:
                text = file.read()
        except FileNotFoundError:
            assert print("The file does not exist.")

        try:
            os.remove(file_to_delete)
        except FileNotFoundError:
            print("The file does not exist.")
        except PermissionError:
            print("You do not have permission to move the file.")

        dirs_path = os.path.dirname(file_to_move)
        if dirs_path:
            os.makedirs(dirs_path, exist_ok=True)

        with open(file_to_move, "w") as file:
            file.write(text)
