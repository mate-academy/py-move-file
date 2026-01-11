import os


def move_file(command_str: str) -> None:
    if (
        len(command_str.split()) != 3
            or command_str[-1] == "/"
            or command_str.split()[0] != "mv"
    ):
        raise AssertionError("Incorrect command asserted")

    command, source_file, file_and_destination = command_str.split()

    if source_file != file_and_destination:
        path = ""
        new_file_name = file_and_destination.split("/")[-1]
        directory_tree = file_and_destination.split("/")[:-1]

        for part in directory_tree:
            path += part + "/"
            os.makedirs(path, exist_ok=True)

        with (
            open(source_file, "r") as file_to_move,
            open(os.path.join(path, new_file_name), "w") as file_to_copy
        ):
            file_to_copy.write(file_to_move.read())
        os.remove(source_file)
