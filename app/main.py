import os


def move_file(command: str) -> None:

    command_upd, file, new_file = command.split()

    if command_upd != "mv" or len(command.split()) != 3:
        raise ValueError("Incorrect command")

    if not os.path.exists(file):
        raise ValueError("File doesn't exist")

    destination_path, new_file_name = os.path.split(new_file)

    if destination_path:
        os.makedirs(destination_path, exist_ok=True)

        with open(file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
        os.remove(file)
    else:
        os.rename(file, new_file)
