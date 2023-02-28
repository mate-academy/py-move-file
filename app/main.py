import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError("Invalid command")
    input_command, old_file_name, new_file_name = command.split()

    if new_file_name.endswith("/") or input_command != "mv":
        raise ValueError("Invalid command")

    separator = new_file_name.rfind("/")
    if separator == -1:
        os.rename(old_file_name, new_file_name)
        return

    destination_folder = new_file_name[:separator]
    os.makedirs(destination_folder, exist_ok=True)
    with (
        open(old_file_name, "r") as file_in,
        open(new_file_name, "w") as file_out
    ):
        file_out.write(file_in.read())

    os.remove(old_file_name)
