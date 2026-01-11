from os import remove, mkdir


def move_file(command: str) -> None:
    _, file, destination = command.split(" ")

    destination_parts = destination.split("/")

    def rename_file(old_file_name: str, new_file_name: str) -> None:
        with open(old_file_name, "r") as file_to_move, \
             open(new_file_name, "w") as destination_file:
            destination_file.write(file_to_move.read())

        remove(file)

    if len(destination_parts) == 1:
        rename_file(file , destination_parts[0])
        return

    for index, _ in enumerate(destination_parts):
        if index == len(destination_parts) - 1:
            rename_file(file, destination)
        else:
            try:
                mkdir("/".join(destination_parts[:index + 1]))
            except FileExistsError:
                continue
